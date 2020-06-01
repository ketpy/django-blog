from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class BlogPost(models.Model):
	Title 	  = models.CharField(max_length = 250)
	CreatedAt = models.DateTimeField(default = timezone.now)
	Post 	  = models.TextField()
	Author    = models.ForeignKey(User, on_delete = models.CASCADE)
	BlogSlug  = models.SlugField(blank = True)
	BlogImage = models.ImageField(upload_to = 'blog')