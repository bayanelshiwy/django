# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Person(models.Model):
    use_in_migrations = True
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Blog(models.Model):
    use_in_migrations = True
    title = models.CharField(max_length=30)
    length = models.CharField(max_length=30)