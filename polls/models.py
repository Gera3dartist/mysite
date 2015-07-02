from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pud_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pud_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class WriterStatusTypeEnum(models.CharField):
    choices = (
        ('new:contact_info_sent', 'new:contact_info_sent'),
        ('new:e_mail_confirmed', 'new:e_mail_confirmed'),
        ('new:test_started', 'new:test_started'),
        ('new:test_passed', 'new:test_passed'),
        ('new:file_sent', 'new:file_sent'),
        ('active:general', 'active:general'),
        ('active:advanced', 'active:advanced'),
        ('active:senior_advanced', 'active:senior_advanced'),
        ('active:premium', 'active:premium'),
        ('active:top_premium', 'active:top_premium'),
        ('active:first_class', 'active:first_class'),
        ('failed:test_essay', 'failed:test_essay'),
        ('failed:no_test_essay', 'failed:no_test_essay'),
        ('failed:gammar_test', 'failed:gammar_test'),
        ('fired:low_quality', 'fired:low_quality'),
        ('fired:plagiarism', 'fired:plagiarism'),
        ('fired:unreliable_writer', 'fired:unreliable_writer'),
        ('fired:invalid_phone', 'fired:invalid_phone'),
        ('fired:multiple_accounts', 'fired:multiple_accounts'),
        ('fired:inappropriate_behavior', 'fired:inappropriate_behavior'),
        ('fired:deactivated_by_writer', 'fired:deactivated_by_writer'),
        ('fired:writer_is_idle', 'fired:writer_is_idle'),
        ('fired:fraud', 'fired:fraud'),
        ('fired:other', 'fired:other'),
    )

    def __init__(self, *args, **kwargs):
        super(WriterStatusTypeEnum, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'writer_status_type'