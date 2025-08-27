from django.db import models

# Create your models here.
class Duty(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title 