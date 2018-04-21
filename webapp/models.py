from __future__ import unicode_literals

from django.db import models

# Модель - "СообщениеИзКосмоса"
class Message(models.Model):
	msg_date = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	readed = models.BooleanField()
	def __str__(self):
		return self.message