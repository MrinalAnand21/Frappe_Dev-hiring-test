from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    # Add other fields here

    class Meta:
        app_label = 'library'


class Member(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields here

    class Meta:
        app_label = 'library'


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issued_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    # Add other fields here

    class Meta:
        app_label = 'library'
