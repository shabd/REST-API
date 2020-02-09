from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """returns a list of API view"""
        an_apiview = [
            'Uses HTTP method as function(get,post,patch ,put ,delete)',
            'Its Similar to a traditional Django view ',
            'Gives you the most control over application logic',
            'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
