from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=1000000)
    description = models.TextField(blank=True)
    author = models.TextField()
    completed = models.BooleanField(default=False)
    started = models.DateField(auto_now_add=True)
    finished = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-started']