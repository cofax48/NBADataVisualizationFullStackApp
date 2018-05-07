from django.db import models

# If I wanted to add models they'd go here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
