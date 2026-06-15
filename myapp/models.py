from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    place_key = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.place_key} ({self.rating} stars)"
