from rest_framework import serializers
from .models import Category, Project, Blog, Faq, TeamCategory, TeamMember, TeamPosition


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"


class TeamPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPosition
        exclude = 'title', 'id'


class TeamMemberSerializer(serializers.ModelSerializer):
    position = TeamPositionSerializer()

    class Meta:
        model = TeamMember
        exclude = 'category', 'order'


class TeamCategorySerializer(serializers.ModelSerializer):
    # members = TeamMemberSerializer(many=True)

    class Meta:
        model = TeamCategory
        exclude = 'title', 'id', 'order'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['members'] = TeamMemberSerializer(instance.members.all(), many=True).data
        return data
