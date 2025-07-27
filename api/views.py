from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post
from post.serializer import PostSerialzer


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
