from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Company import Company


class Employee(models.Model):
    class JobTitles(models.TextChoices):
        ACCOUNTANT = "accountant"
        SOFTWARE_DEVELOPER = "software developer"
        SOFTWARE_TESTER = "software tester"
        MANAGER = "manager"

    name = models.CharField()
    email = models.EmailField()
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18)])
    job_title = models.CharField(choices=JobTitles.choices)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
