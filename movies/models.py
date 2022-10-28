from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
import uuid

from utils.models import Entity

User = get_user_model()


class Category(Entity):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}||{self.name}'
    


class CommonDetail(Entity):
    class Meta:
        abstract = True

    title = models.CharField(max_length=150)
    release_date = models.DateField(db_column='date')
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    is_for_adults = models.BooleanField(default=False)
    trailer_url = models.URLField(null=True, blank=True)


class Movie(CommonDetail):
    is_featured = models.BooleanField(default=False)
    length = models.CharField(max_length=6)
    categories = models.ManyToManyField(Category, related_name='movies')
    image = models.URLField(null=True, blank=True)
    thumbnail = models.URLField(null=True, editable=False)
    user = models.ManyToManyField(User, related_name='favorite_movies', blank=True)

    def __str__(self):
        return self.title

    @property
    def actors(self):
        return self.actors.all()


class Serial(CommonDetail):
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='series')
    image = models.URLField(null=True)
    thumbnail = models.URLField(null=True, editable=False)
    user = models.ManyToManyField(User, related_name='favorite_series', blank=True)

    def __str__(self):
        return self.title

    @property
    def actors(self):
        return self.actors.all()

    @property
    def seasons(self):
        return self.seasons.all()


class Season(Entity):
    number = models.PositiveIntegerField(
        validators=[MinValueValidator(1, message='Minimum season for any series is 1')])
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, related_name='seasons')

    def __str__(self):
        return f'{self.serial.title} || Season {self.number}'


class Episode(CommonDetail):
    number = models.PositiveIntegerField(
        validators=[MinValueValidator(1, message='Minimum season for any episode is 1')])
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    length = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.season} || {self.title}'

    @property
    def actors(self):
        return self.season.serial.actors.all() + self.actors.all()

    @property
    def image(self):
        return self.season.serial.image


class New(Entity):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(db_column='date')
    image = models.URLField(unique=True, null=True)

    def __str__(self):
        return self.title


class Actor(Entity):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    movies = models.ManyToManyField(Movie, related_name='actors', blank=True)
    series = models.ManyToManyField(Serial, related_name='actors', blank=True)
    episodes = models.ManyToManyField(Episode, related_name='guest_actors', blank=True)
    def __str__(self):
        return f'{self.id}||{self.name}||{self.image}'
