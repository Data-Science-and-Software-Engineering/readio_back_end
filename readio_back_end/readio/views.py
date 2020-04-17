from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Ratings, User
from .serializers import BookSerializer, UserSerializer, RatingSerializer


class BookApi(APIView):

    def get(self, request, format=None):
        books = Book.objects.get(id=0)
        serializer = BookSerializer(books)
        return Response(serializer.data)

