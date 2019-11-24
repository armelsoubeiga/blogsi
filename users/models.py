from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Only that User!
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Change to String obj. for simple reading into Admin panel
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Call parent class method and change it
        super().save(*args, **kwargs)

        # Open image in the current instance
        img = Image.open(self.image.path)

        # Check Image and Resize than Save it
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)
