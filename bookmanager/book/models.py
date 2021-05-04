from django.db import models


# Create your models here.
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# people
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # foreignKey
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
