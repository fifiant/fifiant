from django.db import models

class Search(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	pub_date = models.DateTimeField()
	author = models.CharField(max_length=100)
	def __unicode__(self):
		return self.title
