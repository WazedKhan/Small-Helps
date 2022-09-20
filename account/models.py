from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.user