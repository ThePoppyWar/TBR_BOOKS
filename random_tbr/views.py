from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from random_tbr.models import Book
from random_tbr.serializers import BookSerializers


class BookListView(generics.ListAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializers


class BookView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializers

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author', None)
        category = self.request.query_params.get('category', None)

        if author is not None:
            queryset = queryset.filter(authors__name=author)
        if category is not None:
            queryset = queryset.filter(categories__name=category)
        return queryset



