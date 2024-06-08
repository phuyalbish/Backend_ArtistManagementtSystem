from rest_framework import serializers
from album.models import Album, Like, Comment, CommentReply, CommentLike, CommentReplyLike
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
        return obj.likes.filter(is_like=True).count()
    
    def get_likes(self, obj):
        likes = obj.likes.filter(is_like=True)
        return LikeSerializer(likes, many=True, read_only=True).data
    
    def create(self, validated_data):
        return CommentReply.objects.create(**validated_data)




class CommentSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_replies = serializers.SerializerMethodField()
    user = UserSerializer(read_only = True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all(), write_only=True, source='user')
    replies = CommentReplySerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields =  "__all__"
    
    def get_total_likes(self, obj):
        return obj.likes.filter(is_like=True).count()
    
    def get_total_replies(self, obj):
        return obj.replies.count()
    
    def get_likes(self, obj):
        likes = obj.likes.filter(is_like=True)
        return CommentLikeSerializer(likes, many=True, read_only=True).data
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)





class AlbumSerializer(serializers.ModelSerializer):
    
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = "__all__"


    def get_total_likes(self, obj):
        return obj.likes.filter(is_like=True).count()
    
    def get_total_comments(self, obj):
        return obj.comments.count()
    
    def get_likes(self, obj):
        likes = obj.likes.filter(is_like=True)
        return LikeSerializer(likes, many=True, read_only=True).data