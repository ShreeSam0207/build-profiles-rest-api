from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication as token

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

class HelloViewSets(viewsets.ViewSet):
    """Test API View set"""
    serializer_class=serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset=["Uses Action - list,create,retrieve,update,partial update,destroy",
        "Automatically maps to URL Routers",
        "Provide more functionality with less code"]

        return Response({"message" " 'Hello', 'a_viewset": a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msg=f'Hello {name}!'
            return Response({'msg' :  msg})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Hanlde getting an object by its id"""
        return Response({'HTTP Method' : 'GET'})

    def update(self,request,pk=None):
        """Hanlde updating an object"""
        return Response({'HTTP Method' : 'PUT'})

    def partial_update(self, request, pk=None):
        """Handling partial update of an object"""
        return Response({'HTTP Method' : 'PATCH'})

    def destroy(self, requst, pk=None):
        """Handling deleting an object"""
        return Response({'HTTP Method' : 'DELETE'})

class UserprofileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    #token authentication added to set permission so a user can only edit their profiles
    #, is added after token so it gets created as a tuple and gets assigned to authentication_classes
    authentication_classes=(token,)
    #this will configure the UserProfileViewset to use token authentication and
    #add the permissions UpdateOwnProfile. every request made will pass through Permissions.py files
    # and checks if it has has_object_permission function to see if the user has necessary permission
    permission_classes=(permissions.UpdateOwnProfile,)
