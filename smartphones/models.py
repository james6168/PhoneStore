from django.db import models

# Create your models here.


class SmartphoneImage(models.Model):
    file_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="smartphones")

    def __str__(self):
        return self.file_name


class Smartphone(models.Model):
    name = models.CharField(max_length=50, null=True)
    back_camera_mp = models.PositiveSmallIntegerField()
    wide_camera_mp = models.PositiveSmallIntegerField()
    front_camera_mp = models.PositiveSmallIntegerField()
    specs = models.TextField()
    extra = models.TextField()
    operating_system = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    grafical_processor = models.CharField(max_length=50)
    dynamic = models.CharField(max_length=50)
    accumulator = models.PositiveSmallIntegerField()
    sim_count = models.PositiveSmallIntegerField()
    ssd = models.PositiveSmallIntegerField()
    ram = models.PositiveSmallIntegerField()
    external_ssd = models.BooleanField()
    display_size = models.PositiveSmallIntegerField()
    display_type = models.CharField(max_length=50)
    display_resolution = models.CharField(max_length=50)
    case = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    is_available = models.BooleanField()
    description = models.TextField()
    images = models.ManyToManyField(SmartphoneImage, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    smartphones = models.ManyToManyField(Smartphone, blank=True)

    def __str__(self):
        return self.name

