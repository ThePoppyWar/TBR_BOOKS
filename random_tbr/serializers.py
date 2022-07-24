from .models import Author, Book, Category
from rest_framework import serializers


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
