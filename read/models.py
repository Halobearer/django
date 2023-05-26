from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.::::::::::::::::::::::::

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Book(models.Model):
    LANGUAGE_CHOICES = [
        ("Y", 'YORUBA'),
        ("H", 'HAUSA'),
        ("I", 'IGBO'),
        ("E", 'ENGLISH')
    ]

    GENRE_CHOICES = [
        ('FICTION', "FIC"),  # FICTION stays in the db, FIC  will be shown to user
        ('POLITICS', "POL"),
        ('FINANCE', "FIN"),
        ('ROMANCE', "ROM")
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    # Anytime you want to implement one to many,
    # it's in the many part you show the relationship:
    # In this case an author can have many books
    # on_delete means what you want to happen when author is deleted
    # CASCADE means the Information would be kept
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    # "related_name="book_author")  # book_author sets the relationship between Book and Author
    # (if on_delete= models.PROTECT)
    # Foreign Key is used during one to many
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES)
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # def __str__(self):
    #     return f"{self.title} {self.first_name} {self.author.last_name} " \
    #            f"{self.genre} {self.language} {self.price} {self.date_added} {self.isbn}"


# class Genre(models.Model):
#     name = models.CharField(max_length=55)
#
#
# class Language(models.Model):
#     name = models.CharField(max_length=255)


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('RETURNED', 'R'),
        ('BORROWED', 'B')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.PROTECT)  # PROTECT-Date won't be lost # one-to-one relationship


class Author(models.Model):
    first_name = models.CharField(max_length=140, blank=False, null=False)  # blank=False means it must not be empty
    last_name = models.CharField(max_length=155, blank=False,
                                 null=False)  # null=False means field can't be null(it has to do with database)
    email = models.EmailField(blank=True, null=False)  # blank=True means not Compulsory
    date_of_birth = models.DateField(blank=True, null=True)  # blank=True, null= True it will go
    date_of_death = models.DateField(blank=True, null=True)  # null=True means it can be null in the db

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#  Whenever you make changes in your models you must migrate -- python manage.py make migrations Then =>
#  python manage.py migrate
