from rest_framework.generics import (ListAPIView)

from company.models import Category, Project, Blog, Faq, TeamCategory, TeamMember
from company.serializers import CategorySerializer, ProjectSerializer, BlogSerializer, FaqSerializer, \
    TeamMemberSerializer, \
    TeamCategorySerializer


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class TeamCategoryListAPIView(ListAPIView):
    queryset = TeamCategory.objects.all()
    serializer_class = TeamCategorySerializer
