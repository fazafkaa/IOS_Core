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

    pdf = models.FileField(
        upload_to='pdf/',
        blank=True,
        null=True
    )

    content = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

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
    
class Profile(models.Model):

    photo = models.ImageField(
        upload_to='profile/'
    )

    full_name = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=100
    )

    about = models.TextField()

    education = models.TextField()

    skills = models.TextField()

    software = models.TextField()

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    def __str__(self):
        return self.full_name
    
    