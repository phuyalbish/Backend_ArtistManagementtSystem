from rest_framework import serializers
from .models import Users,Artist
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = Users
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Users.objects.create(**user_data, role=Users.ARTIST)
        artist = Artist.objects.create(user=user, **validated_data)
        return artist

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance=instance.user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                raise serializers.ValidationError(user_serializer.errors)
        return super().update(instance, validated_data)