#coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from tinymce.models import HTMLField


@python_2_unicode_compatible
class Contest(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nazwa')
    header_image = models.ImageField(upload_to="logo", null=True, blank=True,
                                     verbose_name='Logo zawodów')
    description = HTMLField(verbose_name='Opis')
    end = models.DateTimeField(verbose_name='Zakończenie zapisów')

    def __str__(self):
        return self.name

    def is_active(self):
        from django.utils import timezone
        return timezone.now() < self.end

    class Meta:
        verbose_name = 'Zawody'
        verbose_name_plural = 'Zawody'


@python_2_unicode_compatible
class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa')
    capacity = models.IntegerField(verbose_name='Ilość zawodników')
    contest = models.ForeignKey(Contest, verbose_name='Zawody')

    def __str__(self):
        return "{0} {1}/{2}".format(self.name, self.contestants_count,
            self.capacity)

    class Meta:
        verbose_name = 'Grupa'
        verbose_name_plural = 'Grupy'

    @property
    def contestants_count(self):
        return self.contestant_set.all().count()


@python_2_unicode_compatible
class Contestant(models.Model):
    GENDER_CHOICES = (
        ('K', 'Kobieta'),
        ('M', 'Mężczyzna')
    )
    SHIRT_SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL')
    )
    first_name = models.CharField(max_length=150, verbose_name='Imię')
    surname = models.CharField(max_length=150, verbose_name='Nazwisko')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              verbose_name='Płeć')
    age	= models.IntegerField(verbose_name='Wiek', null=True, blank=True)
    email = models.EmailField(verbose_name='Adres e-mail')
    sponsor = models.CharField(max_length=200, verbose_name='Klub/sponsor')
    group = models.ForeignKey(Group, verbose_name='Grupa')
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZE_CHOICES,
                                  verbose_name='Rozmiar koszulki')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.surname)

    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'
