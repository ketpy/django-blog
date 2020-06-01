from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
	user 	    = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
	created_on  = models.DateTimeField(default = timezone.now)
	ProfilePic  = models.ImageField(upload_to = 'profile', blank = True, default = 'assets/default.jpg')

	def save(self, *args, **kwargs):
		super().save()
		img = Image.open(self.ProfilePic.path)
		if img.height > 200 or img.width > 250:
			new_img = (200, 250)
			img.thumbnail(new_img)
			img.save(self.ProfilePic.path) 

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		profile = UserProfile.objects.create(user=instance)
		profile.save()