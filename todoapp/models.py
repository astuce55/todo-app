from django.db import models

# Create your models here.
class task(models.Model):
    Title = models.CharField(max_length=200)
    Time = models.DateTimeField(auto_now=True)
    Complete = models.BooleanField(default=False)
    Deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Title