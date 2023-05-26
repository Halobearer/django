from decimal import Decimal

from rest_framework import serializers

from .models import Author, Book
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


# We define the Fields we wish to serialize
# This will hold the data we would ant to show the user

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


#    OR
#     first_name = serializers.CharField(max_length=255)
#     last_name = serializers.CharField(max_length=255)
#     date_of_birth = serializers.DateField()


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer() #  can be used for hyperlink

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description',
                  'discounted_price', 'author', 'price']

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail'
    )

    discounted_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price * Decimal(0.5)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# title = serializers.CharField(max_length=255)
# # author = serializers.
# # isbn = book_number
# # isbn = serializers.CharField(max_length=13)
# #   OR
# book_number = serializers.CharField(max_length=13, source='isbn')
# description = serializers.CharField(max_length=255)
# # date_added = serializers.DateTimeField()
# genre = serializers.CharField(max_length=15)
# language = serializers.CharField(max_length=15)
# price = serializers.DecimalField(max_digits=6, decimal_places=2)
