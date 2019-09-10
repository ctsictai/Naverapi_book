from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)
    states = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
