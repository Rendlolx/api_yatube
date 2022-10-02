from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'post',
            'comment'
        )
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='slug',
        required=False,
        queryset=Group.objects.all(),
    )
    publication_date = serializers.DateTimeField(
        read_only=True,
        source='pub_date'
    )
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'text',
            'publication_date',
            'author',
            'image',
            'group',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'title',
            'slug',
            'description',
        )


class CommentSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(
        read_only=True,
        source='created'
    )
    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'post',
            'text',
            'created_date',
        )
