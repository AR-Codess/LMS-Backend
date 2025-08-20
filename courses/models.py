from django.db import models
from academics.models import CourseClass
from academics.models import CourseClass
from courses.models import Course

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title