from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(default=None, upload_to='video')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title
