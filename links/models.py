from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.
# sava a shortened link - name, url, slug, # of clicks

class Link(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    # increment "clicks" by 1 everytime someone clicks on it
    def click(self):
        self.clicks += 1
        self.save()

    # automatically slug the name using slugify if no slug entered 
    # slugify will turn " " into "-"
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)