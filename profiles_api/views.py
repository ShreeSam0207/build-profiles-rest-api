from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiview(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of API View features"""
        an_apiview=[
        'Uses HTTP Methods as function (get,patch,put,post,delete)',
        'Is similar to traditional Django view',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLS'
        ]

        return Response({'message' : 'Hello','an_apiview' : an_apiview})
