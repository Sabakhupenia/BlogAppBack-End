from rest_framework import viewsets
from Blogs.models import BlogPost
from Blogs.serializers import BlogPostSerializer

class PopularBlogsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Query for popular blogs (customize your criteria)
        popular_blogs = BlogPost.objects.filter(views__gte=10)  # Example: Blogs with 10 or more views
        return popular_blogs

class NewBlogsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        # Query for new blogs (customize your criteria)
        new_blogs = BlogPost.objects.order_by('-date_published')[:10]  # Example: Latest 10 blogs
        return new_blogs


class BlogsByTopicViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        # Query for blogs related to the specified topic
        blogs_by_topic = BlogPost.objects.filter(topics__id=topic_id)
        return blogs_by_topic
