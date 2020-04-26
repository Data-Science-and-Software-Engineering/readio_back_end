from .models import Book, Ratings, User
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'book_title', 'book_author', 'year_of_publication',
                  'publisher', 'image_url_s', 'image_url_m', 'image_url_l']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['user_id', 'ISBN', 'book_rating']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'location', 'age']