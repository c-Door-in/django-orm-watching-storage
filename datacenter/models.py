import time
from datetime import datetime
from django.db import models
from django.utils.timezone import localtime, make_aware


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )


def get_duration(visit):
    local_entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        end_time = visit.leaved_at
    else:
        end_time = make_aware(datetime.today())
    return (end_time - local_entered_at).total_seconds()


def format_duration(duration):
    return time.strftime('%H:%M:%S', time.gmtime(duration))


def is_visit_long(visit, minutes=60):
    return (get_duration(visit) / 60) >= minutes