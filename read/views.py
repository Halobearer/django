from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .pagination import DefaultPagination
from .serializer import AuthorSerializer, BookSerializer

from .models import Author, Book
from .filters import AuthorFilter, BookFilter


# FUNCTION BASE VIEW

# Create your views here.
# THE LOGIC

# def welcome(request):
#     return HttpResponse('ok')
#
#
# def welcome2(request):
#     return HttpResponse('welcome')

# ====================================
# ====================================
# @api_view(['GET', 'POST', 'DELETE'])
# def display_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()  # To display all authors
#         serializers = AuthorSerializer(authors,
#                                        many=True)  # many=True - means it will be expecting many authors/resources
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         #  Now we Deserialize
#         serialize = AuthorSerializer(
#             data=request.data)  # deserializing- it collects the JSON and converts to python object
#         serialize.is_valid(raise_exception=True)
#         # serialize.validated_data()
#         serialize.save()
#         return Response("success", status=status.HTTP_201_CREATED)

# class AuthorList(ListCreateAPIView):  # An Easier way of doing Class Base Model
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# The Longer method of the code at AuthorList up
# def get_queryset(self):
#     return Author.objects.all()
#
# def get_serializer_class(self):
#     return AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination  # Custom Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'price']


class AuthorView(APIView):
    def get(self):
        authors = Author.objects.all()  # To display all authors
        serializers = AuthorSerializer(authors,
                                       many=True)  # many=True - means it will be expecting many authors/resources
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialize = AuthorSerializer(
            data=request.data)  # deserializing- it collects the JSON and converts to python object
        serialize.is_valid(raise_exception=True)
        # serialize.validated_data()
        serialize.save()
        return Response("success", status=status.HTTP_201_CREATED)


# To get a particular Author
# CLASS BASE VIEW

class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("detail updated", status=status.HTTP_200_OK)

    def delete(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])  # (['POST', 'PUT'])  # Methods to be allowed
def author_detail(request, pk):
    if request.method == 'GET':
        author = get_object_or_404(Author, pk=pk)
        # author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)  # object gets passed into the serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':  # editing
        author = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("details updated", status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        author = get_object_or_404(Author, pk=pk)
        # if author.book_author.count() > 0:  # How to handle a PROTECTED SITUATION
        #     return Response({"error": "Author associated with a book cannot be deleted"},
        #                     status=status.HTTP_405_METHOD_NOT_ALLOWED)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {"request": self.request}


@api_view(['GET', 'POST'])
def display_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializers = BookSerializer(books, many=True, context={'request': request})  # context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("success", status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def book_detail(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        serializers = BookSerializer(book, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Details updated", status=status.HTTP_200_OK)

# CLASS BASE VIEW
