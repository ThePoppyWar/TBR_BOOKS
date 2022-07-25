from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from random_tbr.models import Book
from random_tbr.serializers import BookSerializers


class BookListView(generics.ListAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializers


class BookView(generics.RetrieveUpdateDestroyAPIView):
    model = Book.objects.all()
    serializer_class = BookSerializers

