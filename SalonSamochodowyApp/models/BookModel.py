from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta
from datetime import date

class Book(models.Model);
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    borrow_count = models

def

def is_popular(self):
    return self.borrow_count > 100

def is_new_relesase(self):
    return (datetime.now().date() - self.published_date) <= timedelta(days=730)

def string_representatin(self):
    return f"(self.title) by {self.author}"

def get_absolute_url(self):
    return.reverse(viewname:'book-details', kwargs=('pk'))


def reverse(self)
    self.avilable = False
    self.save()
