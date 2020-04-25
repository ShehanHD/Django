from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class quotes(models.Model):
    quote = RichTextField();
    book = models.CharField(max_length=100)
    verse = models.IntegerField()
    fro = models.IntegerField()
    to = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.book
    