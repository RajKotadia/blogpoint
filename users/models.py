from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='default.png', upload_to='profile_pics')
	bio = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.user.username

	# override the default save() to resize the image and then save
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.profile_image.path)

		if img.height > 200 or img.width > 200:
			output_size = (200, 200)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)
