from django.core import validators
from django.db import models

from fruitexam.fruitexam_app.validators import first_letter_validator, only_letters_validator


class ProfileModel(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        validators=(
            validators.MinLengthValidator(2),
            first_letter_validator,
        ),
        # verbose_name='First Name'

    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=35,
        validators=(
            validators.MinLengthValidator(1),
            first_letter_validator,
        ),
        # verbose_name='Last Name'
    )
    email = models.EmailField(
        blank=False,
        null=False,
        max_length=40,
        # verbose_name='Email'
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        ),
        # verbose_name='Password'
    )
    image_url = models.URLField(
        null=True,
        blank=True
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )


class FruitModel(models.Model):

    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            only_letters_validator
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        # verbose_name='Image URL',
    )
    description = models.TextField(
        null=False,
        blank=False
    )
    nutrition = models.TextField(
        null=True,
        blank=True
    )



