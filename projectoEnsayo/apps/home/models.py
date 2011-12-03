from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length = 300)
	autor = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	main_content = models.TextField()

	def __unicode__(self):
		return self.title