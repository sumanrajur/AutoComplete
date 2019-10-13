from django.db import models

# Create your models here.
class Word_Freq(models.Model):
  """
  Stores a Word and Frequency of the Word into the DB.
  """
  word = models.CharField(max_length=50)
  freq = models.IntegerField()
  def __str__(self):
    return self.word