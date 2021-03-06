from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiview(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        'Uses HTTP Methods as function (get,patch,put,post,delete)',
        'Is similar to traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLS'
        ]
        return Response({'message' : 'Hello','an_apiview' : an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        #this data is passed to serializer class that comes with API view
        serializer=self.serializer_class(data=request.data)
        #validating the data in Serializer
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello {name}'
            return Response({'msg' : msg})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method ': 'PUT'})

    def patch(self,request,pk=None):
        """"Handle partial update of an object"""
        return Response({'method ': 'PATCH'})


    def delete(self,request,pk=None):
        """Handle deletion of an object"""
        return Response({'method ': 'DELETE'})
