from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class gallery(models.Model):
    Event = models.CharField( max_length=50)
    img = models.ImageField(upload_to='pics/gallery', default='pics/gallery/default.jpg')
    description = RichTextField()
    onMainPage = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.description
