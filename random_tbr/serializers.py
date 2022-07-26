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
    authors = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())
    categories = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ("title", "authors", 'categories', 'cover', 'average_rating', 'thumbnail')



