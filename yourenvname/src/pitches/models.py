from django.db import models

# Create your models here.
class pitches(models.Model):
	#image			= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	name 			= models.CharField(max_length=120)
	category 		= models.CharField(max_length=120)
	description 	= models.TextField(blank=True, null=True)
	date 			= models.DateField(auto_now=False, auto_now_add=True)
	likedBy 		= models.TextField()
	dislikedBy 		= models.TextField()
	tags 			= models.TextField()
	likeCounter		= models.PositiveIntegerField()
