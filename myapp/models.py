from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=100)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name


class File(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('text', 'Text'),
        ('pdf', 'PDF'),
    ]

    folder = models.ForeignKey(
        Folder,
        on_delete=models.CASCADE,
        related_name='files'
    )

    name = models.CharField(max_length=200)

    file_type = models.CharField(
        max_length=20,
        choices=FILE_TYPES
    )

    image = models.ImageField(
        upload_to='files/',
        blank=True,
        null=True
    )

    content = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name