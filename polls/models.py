from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pud_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Reader(models.Model):
    comment = models.CharField(max_length=300)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.comment

class Topping(models.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)

##############
# Tutorial: django site
# https://docs.djangoproject.com/en/1.8/topics/db/models/

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, related_name='musicant', related_query_name='musicants')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_start = models.IntegerField()

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

#############################
# learning many to many relationships,
# using tables for governing relation
class PersonArtist(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(PersonArtist, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(PersonArtist, related_name='membership')
    group = models.ForeignKey(Group, related_name='membership')
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


#############################
# Multitable inheritance
# using PersonArtist class

class Moderator(PersonArtist):
    serves_talk_show = models.BooleanField(default=False)
    prev_channel = models.CharField(max_length=50)

#############################
# Making queries
# https://docs.djangoproject.com/en/1.8/topics/db/queries/#falling-back-to-raw-sql

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline







