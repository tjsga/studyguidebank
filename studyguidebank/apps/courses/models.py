from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator

# Create your models here.
class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)
    url = models.CharField(max_length=20, unique = True, validators=[RegexValidator(regex="^[a-zA-Z0-9_\-]+$", message="Only alphanumeric, dashes, and underscores allowed")])

    courses = models.ManyToManyField("Course", related_name="subject")

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, unique = True)

    units = models.ManyToManyField("Unit", related_name="course")

    def __str__(self):
        return self.name

class Unit(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)

    pdf_file = models.FileField(upload_to='guides/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return self.name



