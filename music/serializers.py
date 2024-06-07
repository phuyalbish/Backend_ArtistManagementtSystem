from rest_framework import serializers, viewsets
from music.models import Music, Like, Comment
from user.models import Users



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'firstname', 'img_profile')  

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'music') 

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields =  "__all__"
class CommentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =  "__all__"


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MusicSerializer(serializers.ModelSerializer):
    
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = "__all__"


    def get_total_likes(self, obj):
        return obj.like_set.count()
    
    def get_total_comments(self, obj):
        return obj.comment_set.count()



