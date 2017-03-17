import datetime

from django.db import models

# Create your models here.
from decimal import Decimal
from . import config


class Centre(models.Model):
    id = models.AutoField(primary_key=True)
    
    def get_income(self, end_date=None, start_date=None, time_delta=datetime.timedelta(days=config.default_period_days)):
        """Calculates the income of a centre within the specified time period.
        start_date trumps time_delta
        """
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is None:
            start_date = end_date - time_delta
        transactions = Transaction.objects.all().filter(learner__centre__id=self.id,
                                                  timestamp__range=['{:%Y-%m-%d}'.format(start_date), '{:%Y-%m-%d}'.format(end_date)])  
        return sum([transaction.amount for transaction in transactions])

    def get_active_students(self, end_date=None, start_date=None, time_delta=datetime.timedelta(days=config.default_period_days)):
        if end_date is None:
            end_date = datetime.date.today()
        if start_date is None:
            start_date = end_date - time_delta
        learners = self.learner_set.all()
        return len([learner for learner in learners if (learner.get_current_credit() > 0) and
                                    len(learner.experience_set.all().filter(recording_time__range=[start_date, end_date]))>0])


    def get_attrition_rate(self, end_date=None, time_period=datetime.timedelta(days=config.default_period_days)):
        if end_date is None:
            end_date = datetime.date.today()
        return -(self.get_active_students(end_date=end_date, time_delta=time_period) -\
                 self.get_active_students(end_date=end_date-time_period, time_delta=time_period))

    def get_conversion_rate(self, end_date=None, start_date=None, time_delta=datetime.timedelta(days=config.default_period_days)):
        #Number registered
            #First session is registration
        #transactions  = reversed(Transaction.objects.all().order_by('id', 'timestamp'))
        #id_time = [(t.id, t.timestamp) for t in transactions]
        
        learners = self.learner_set.all().annotate(registration=models.Min('transaction__timestamp')).filter(registration__range=[start_date, end_date])

        #Number who bought credit
            #credits > 0
        learners = [learner for learner in learners if len(Transaction.objects.all().filter(credits__gt=0, learner=learner))>0]
        
        return sum(learners)

        

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

    def get_current_credit(self):
        transactions = Transaction.objects.filter(learner__id=self.id)
        return sum([transaction.credits for transaction in transactions])


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
