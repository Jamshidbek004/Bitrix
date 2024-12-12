from django.db import models

class Viloyat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Aperator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Royxat(models.Model):
    STATUS_CHOICES = [
        ('RO', 'Royxatga olingan'),
        ('YT', 'Yetkazib berishga tayyor'),
        ('YB', 'Yetkazib berildi'),
        ('BK', 'Bekor qilingan'),
    ]

    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    viloyat = models.ForeignKey(Viloyat, models.CASCADE)
    tuman = models.CharField(max_length=100)
    mahhala = models.CharField(max_length=200)
    raqam = models.IntegerField()
    kilent = models.IntegerField()
    sharx = models.TextField(null=True)
    aperator = models.ForeignKey(Aperator, models.CASCADE)
    royxat_vaqti = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RO')

    def __str__(self):
        return f"{self.ism} ({self.get_status_display()})"
