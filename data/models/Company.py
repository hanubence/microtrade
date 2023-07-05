from django.db import models


class Company(models.Model):
    name = models.CharField("Name of the company")
    email = models.EmailField("E-mail address of the company")
    description = models.TextField(
        "Text description of the company", null=True, blank=True
    )
