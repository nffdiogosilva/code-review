# Not requested, but added module serializeres
# to display where I would handle the object validation and its creation,
# and to be able to see the whole workflow.
# August 12, 2019
# Nuno Diogo da Silva (diogosilva.nuno@gmail.com)
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'confirm_password', 'comment']

    # This is where I would create the object,
    # and not directly through the User objects Manager, inside the view,
    # like it's being done on the views_original.py file.
    def create(self, validated_data):
        del validated_data["confirm_password"]
        user = User.objects.create_user(validated_data['username'],
                                        email=validated_data['email'],
                                        password=validated_data['password'])
        return user

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords don't match.")
        return data
