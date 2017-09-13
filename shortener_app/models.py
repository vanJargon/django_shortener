from __future__ import unicode_literals

from django.db import models
# from django.utils import timezone

# Create your models here.
class URLRecord(models.Model):
	original_url = models.TextField()

	def retrieve_url(self):
		return self.original_url




