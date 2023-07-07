from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Company import Company


class Employee(models.Model):
    class JobTitles(models.TextChoices):
        ACCOUNTANT = "accountant"
        SOFTWARE_DEVELOPER = "software developer"
        SOFTWARE_TESTER = "software tester"
        MANAGER = "manager"

    name = models.CharField("Full name of the employee", max_length=40)
    email = models.EmailField("E-mail address of the employee")
    age = models.PositiveIntegerField(
        "Age of the employee, must be at least 18",
        default=18,
        validators=[MinValueValidator(18)],
    )
    jobTitle = models.CharField(
        "Job title of the employee", choices=JobTitles.choices, max_length=20
    )
    company = models.ForeignKey(
        Company,
        verbose_name="Place of employment of the employee",
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
