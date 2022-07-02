from operator import mod
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length=200)

    description = models.CharField(max_length=200)

    identifier = models.SlugField(blank=True, unique=True)

    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
    )

    created_date = models.DateTimeField()

    active = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    #     pass 

