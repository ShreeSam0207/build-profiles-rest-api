from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """"Serializes a name field for testing our APIView"""

    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        #make password filed write only
        extra_kwargs={
            'password' : {
                'write_only' : True,
                'style' : {
                    'input_type' : 'password'
                    }
                }
        }

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

        def update(self,instance,validated_data):
            """handle updating user accoumt"""
            if 'password' in validated_data:
                password=validated_data('password')
                instance.set_password(password)

            return super().update(insatnce,valdiated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed item"""
    class Meta:
        model=models.ProfileFeedItem
        #make these fields available through serializer
        #by default Django creates the primary field key for the models we create and is set to read only
        #created on is automatically set, by default this will also be read only
        #hence here user profile and status text will be write only
        fields=('id','user_profile','status_text','created_on')
        #we want to make sure user profile is updated only by the authenticated user and not anybody ModelSerializer
        # hence we make this user profile read only
        extra_kwargs= {
            'user_profile' : {'read_only' : True}
        }
