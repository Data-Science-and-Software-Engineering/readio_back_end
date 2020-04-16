from django.db import models


class Book(models.Model):
    ISBN = models.TextField()
    book_title = models.TextField()
    book_author = models.TextField()
    year_of_publication = models.IntegerField()
    publisher = models.TextField()
    image_url_s = models.TextField()
    image_url_m = models.TextField()
    image_url_l = models.TextField()


class User(models.Model):
    user_id = models.IntegerField()
    location = models.TextField()
    age = models.IntegerField()


class Ratings(models.Model):
    user_id = models.IntegerField()
    ISBN = models.TextField()
    book_rating = models.IntegerField()
