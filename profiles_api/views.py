from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test Api View"""
    # have to add this in order to add the post function
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of API view"""
        an_apiview = [
            'Uses HTTP method as function(get,post,patch ,put ,delete)',
            'Its Similar to a traditional Django view ',
            'Gives you the most control over application logic',
            'Its mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name """
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handel updating an object """
        return Response({'method': "PUT"})

    def patch(self, request, pk=None):
        """Handles partial update of an object """
        return Response({'method': "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test APi View set """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello Message """
        a_viewset = [
            'Uses actions (list , create ,retrieve ,update ,partial_update',
            'Automatically maps to Urls using Routers ',
            'Provides more functionality with less code  ',
        ]
        return Response({'message': 'List', 'a_View': a_viewset})

    def create(self, request):
        """create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            surname = serializer.validated_data.get('surname')
            message = f'hello {name} ,{surname} !'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID """
        return Response({'HTTP GET': "GET"})

    def update(self, request, pk=None):
        """Handels updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, reqest, pk=None):
        """updates partial update"""
        return Response({'Http_method ': 'Patch'})

    def destroy(sel, request, pk=None):
        """handles removing an object """
        return Response({'http_method': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handel creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # add comma afterwards , to insure it gets creted as a tupel
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)  # allow to search for a user
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handel creating user authentications """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    # this makes sure that you can only create or update a status on your own profile
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

