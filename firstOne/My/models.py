from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# One main Chai model
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='My/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# One-to-many: Each ChaiVariety can have many reviews
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


# Many-to-many: Each store can sell multiple chai varieties, and each chai can appear in many stores
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name


# One-to-one: Each chai has a unique certificate
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
