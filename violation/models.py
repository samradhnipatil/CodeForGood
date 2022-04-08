from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Violation(models.Model):
	text = models.CharField(max_length=500)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text
