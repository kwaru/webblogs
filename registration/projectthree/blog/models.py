from django.db import models

# Create your models here.
class Post(models.Model):
	""""a post a user has posted"""
	text=models.CharField(max_length=500)
	date_posted=models.DateTimeField(auto_now_add=True)


	def __str__(self):

		"""returns users string representation of the post"""
		return self.text


class Entry(models.Model):
	"""this is a class for entries about the posts"""
	post=models.ForeignKey(Post, on_delete=False)
	text=models.TextField()
	post_date=models.DateTimeField(auto_now_add=True)


	class Meta:
	  verbose_name_plural='entries'



	def __str__(self):

		return self.text[:50]+"........"

