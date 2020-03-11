from django.db import models

class ppost(models.Model):
	titel=models.CharField(max_length=255)
	bodey=models.TextField()


