from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIViews"""
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=50)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serialiser a user profile object """

    class Meta:
        model = models.UserProfile  # telling Meta what class from models to use
        # listing all the class we want to add in
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {  # to make  out password a secret
            'password': {
                'write_only': True,  # can only use password to create users , not retrieve
                'style': {'input_type': 'password'}  # doesnt show password as we type it
            }
        }

        def create(self, validate_data):
            """create and return a new user"""
            user = models.UserProfile.objects.create_user(
                email=validate_data('email'),
                name=validate_data('name'),
                password=validate_data('password'),

            )
            return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}