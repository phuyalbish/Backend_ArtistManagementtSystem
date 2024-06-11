from rest_framework import serializers
from music.models import Music, Like, Comment, CommentReply, CommentLike, CommentReplyLike
from user.models import Users



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'firstname', 'img_profile')  


class CommentReplyLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    class Meta:
        model = CommentReplyLike
        fields = "__all__"
    def create(self, validated_data):
        return CommentReplyLike.objects.create(**validated_data)


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    class Meta:
        model = CommentLike
        fields = "__all__"
    def create(self, validated_data):
        return CommentLike.objects.create(**validated_data)


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    class Meta:
        model = Like
        fields = "__all__"
    def create(self, validated_data):
        return Like.objects.create(**validated_data)



class CommentReplySerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    likes = serializers.SerializerMethodField()
    class Meta: 
        model = CommentReply
        fields = "__all__"

    def get_total_likes(self, obj):
        return obj.music_comment_reply_likes.filter(is_like=True).count()
    
    def get_likes(self, obj):
        music_comment_reply_likes = obj.music_comment_reply_likes.filter(is_like=True)
        return CommentReplyLikeSerializer(music_comment_reply_likes, many=True, read_only=True).data
    
    def create(self, validated_data):
        return CommentReply.objects.create(**validated_data)




class CommentSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_replies = serializers.SerializerMethodField()
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    music_comment_replies = CommentReplySerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields =  "__all__"
    
    def get_total_likes(self, obj):
        return obj.music_comment_likes.filter(is_like=True).count()
    
    def get_total_replies(self, obj):
        return obj.music_comment_replies.count()
    
    def get_likes(self, obj):
        music_comment_likes = obj.music_comment_likes.filter(is_like=True)
        return CommentLikeSerializer(music_comment_likes, many=True, read_only=True).data
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)





class MusicSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    album_name = serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Music
        fields = "__all__"

    def get_total_likes(self, obj):
        return obj.music_likes.filter(is_like=True).count()

    def get_total_comments(self, obj):
        return obj.music_comments.count()

    def get_likes(self, obj):
        music_likes = obj.music_likes.filter(is_like=True)
        return LikeSerializer(music_likes, many=True, read_only=True).data

    def get_album_name(self, obj):
        return obj.album.name if obj.album else None

    def get_artist_name(self, obj):
        return obj.artist.firstname if obj.artist else None
    



# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

