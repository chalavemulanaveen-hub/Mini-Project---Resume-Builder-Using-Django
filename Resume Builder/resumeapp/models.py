from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    title = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    address = models.TextField()

    summary = models.TextField()

    education = models.TextField()

    experience = models.TextField()

    skills = models.TextField()

    template = models.CharField(max_length=20)

    def __str__(self):
        return self.name