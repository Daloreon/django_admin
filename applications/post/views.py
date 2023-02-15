from django.shortcuts import render
from rest_framework.viewsets import generics
from applications.post.models import Post ,PostImage, Comments
from applications.post.serializers import PostSerializer, PostImageSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from applications.post.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from applications.feedback.models import Like, Rating
from applications.feedback.serializer import RetingSerializer

# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostCreateAPIView(generics.CreateAPIView):
#     serializer_class = PostSerializers


# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers



# class PostDeleteAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


# class PostDetailAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     lookup_field = 'id'

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size =100000



# class PostlistCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsOwner] 
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = CustomPagination

#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['owner','title']
#     # filter_field = 'all'
#     search_fields = ['title']
#     ordering_fields = ['id']

#     # def get_queryset(self):
#     #     queruset = super().get_queryset()
#     #     # queruset = queruset.filter(owner=5)   
#     #     filter_owner = self.request.query_params.get('owner')
#     #     if filter_owner:
#     #         queruset = queruset.filter(owner = filter_owner)
#     #     return queruset

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# class PostDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwner]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class CreateImageAPIView(generics.CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class =  PostImageSerializer
    permission_classes = [IsAuthenticated]



class CommentsViewSet(ViewSet):
    def list(self, request):
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class CommentModeViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    pagination_class = CustomPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['owner', 'title']
    search_fields = ['title']
    ordering_fields = ['id', 'owner']
    


    @action(methods=['POST'], detail=True)            # localhost:8000/api/v1/post/1/like по такому пути отработает наша функция like
    def like(self, request, pk, *args, **kwargs):
        user = request.user
        like_obj, _ = Like.objects.get_or_create(owner=user, post_id=pk)
        like_obj.is_like = not like_obj.is_like
        like_obj.save()
        status = 'liked'

        if not like_obj.is_like:
            status = 'unliked'
        return Response({'status': status})
    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializer = RetingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating_obj, _ = Rating.objects.get_or_create(owner=request.user, post_id=pk,)
        rating_obj.rating = request.data['rating']
        rating_obj.save()
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
