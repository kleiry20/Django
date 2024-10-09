# tells python how to transform model into json data that we can access in our API
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    # this specifies which 'model' and 'fields' we want to transform
    # in this case = User model + all fields in User model
    class Meta:
        model = User
        fields = '__all__'