from django.db import models
from django.contrib.auth.models import User


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserAddress")
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="UserProfile")
    mobile = models.CharField(max_length=10)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE, related_name="UserAddresses")
    profile_picture = models.ImageField(null=True, blank=True, upload_to='user_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)