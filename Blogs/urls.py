from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from Readinglist.views import PopularBlogsViewSet, NewBlogsViewSet, BlogsByTopicViewSet
from Blogs.views import BlogPostViewSet
# Create a router
router = DefaultRouter()

# Register your viewset with the router
router.register(r'popular-blogs', PopularBlogsViewSet, basename='popular-blog')
router.register(r'new-blogs', NewBlogsViewSet, basename='new-blog')
router.register(r'blog-posts', BlogPostViewSet, basename='blog-post')  # Register BlogPostViewSet


urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
    # Define a URL pattern for blogs by topic
    re_path(r'^blogs-by-topic/(?P<topic_id>\d+)/$', BlogsByTopicViewSet.as_view({'get': 'list'}), name='blogs-by-topic'),
]


