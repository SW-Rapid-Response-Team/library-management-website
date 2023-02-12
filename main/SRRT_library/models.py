from django.db import models
from isbn_field import ISBNField
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    subject = models.CharField(max_length=64)
    isbn = ISBNField(primary_key=True)
    author = models.CharField(max_length=64)

    COMPUTER_GENERAL = 'CG'
    PHILOSOPHY_PSYCHOLOGY = 'PP'
    RELIGION = 'RE'
    SOCIAL = 'SO'
    LANGUAGE = 'LA'
    SCIENCE = 'SC'
    TECHNOLOGY = 'TE'
    ARTS_RECREATION = 'AR'
    LITERATURE = 'LI'
    HISTORY_GEOGRAPHY = 'HG'

    BOOK_CATEGORIES = [
        (COMPUTER_GENERAL, 'COMPUTER_GENERAL'),
        (PHILOSOPHY_PSYCHOLOGY, 'PHILOSOPHY_PSYCHOLOGY'),
        (RELIGION, 'RELIGION'),
        (SOCIAL, 'SOCIAL'),
        (LANGUAGE, 'LANGUAGE'),
        (SCIENCE, 'SCIENCE'),
        (TECHNOLOGY, 'TECHNOLOGY'),
        (ARTS_RECREATION, 'ARTS_RECREATION'),
        (LITERATURE, 'LITERATURE'),
        (HISTORY_GEOGRAPHY,'HISTORY_GEOGRAPHY')
    ]
    kinds_of_books = models.CharField(
        max_length=2,
        choices=BOOK_CATEGORIES,
        default=COMPUTER_GENERAL,
    )
    
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.subject


class CheckoutLog(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateTimeField()#null=True, blank=True

