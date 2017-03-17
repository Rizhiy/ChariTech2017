from django.db import models

# Create your models here.
from decimal import Decimal


class Centre(models.Model):
    id = models.AutoField(primary_key=True)


class Learner(models.Model):
    id = models.BigAutoField(primary_key=True)
    centre = models.ForeignKey(Centre)
    date_joined = models.DateTimeField(null=True)
    language = models.TextField(null=True)
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True)
    date_of_birth = models.DateTimeField(null=True)
    grade_at_registration = models.IntegerField(null=True)
    family_size = models.IntegerField(null=True)
    father_occupation = models.TextField(null=True)
    mother_occupation = models.TextField(null=True)


class Experience(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.IntegerField(null=True)
    learner = models.ForeignKey(Learner)
    score = models.IntegerField(null=True)
    answer_value = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(null=True)
    latency = models.IntegerField(null=True)
    recording_time = models.DateTimeField(null=True)

class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    learner = models.ForeignKey(Learner)
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    credits = models.DecimalField(max_digits=20, decimal_places=2, )
    #credit_balance = models.DecimalField(max_digits=20, decimal_places=2, )


# class Session(models.Model):
#     id = models.AutoField(primary_key=True)
#     learner = models.ForeignKey(Learner)
#     ip_address = models.TextField(null=True)
#     mac_address = models.TextField(null=True)
#     battery_level = models.IntegerField(null=True)
#     expire_date = models.DateTimeField()


# class Diamond(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     quantity = models.IntegerField(null=True)
#     timestamp = models.DateTimeField()
#     learner = models.ForeignKey(Learner)


# class Synchronisation(models.Model):
#     centre = models.ForeignKey(Centre)
#     filename = models.CharField(unique=True, max_length=30)
#     generated_at = models.DateTimeField()
#     synced_at = models.DateTimeField()
#     success = models.BooleanField()
#     filesize = models.FloatField()
#
#     class Meta:
#         db_table = 'synchronisation'
