from django.db import models


class Image(models.Model):
    src = models.ImageField(
        upload_to="media/images", 
    )
    description = models.TextField(
        verbose_name="Descrição",
        max_length=250
    )