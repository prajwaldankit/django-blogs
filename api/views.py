from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post, Comment
from post.serializer import PostSerialzer, CommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import authentication, permissions


class ListPosts(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        posts = Post.objects.all().select_related('category')
        serializer = PostSerialzer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serialzer = PostSerialzer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "success": True
            })

        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            "errors": serialzer.errors,
            "success": False
        })


class PostDetail(APIView):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serilaizer = PostSerialzer(post)

        return Response({
            "success": True,
            "data": serilaizer.data
        })


@api_view(['GET'])
def api_index(request):
    result = {
        "foo": "bar"
    }
    return Response(result)


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all().select_related('category')
    serializer = PostSerialzer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_all_comments(request):
    posts = Comment.objects.all()
    serializer = CommentSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_comments_for_post_by_slug(request, slug):

    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)
    posts = Comment.objects.all()
    serializer = CommentSerializer(posts, many=True)

    return Response(serializer.data)
