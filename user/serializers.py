from rest_framework import serializers
from .models import Users
from customizeable.models import CustomThemeSerializer
class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    theme = CustomThemeSerializer(read_only=True) 
    total_music = serializers.SerializerMethodField()
    total_album = serializers.SerializerMethodField()
    class Meta:
        model = Users
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data.setdefault('gender', 0)
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    def get_total_music(self, obj):
        return obj.artist_music.filter(is_deleted=False).count()
    
    def get_total_album(self, obj):
        return obj.artist_album.filter(is_deleted=False).count()

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    