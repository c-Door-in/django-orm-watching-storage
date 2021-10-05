from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        this_passcard_visit = {
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit)
        }
        this_passcard_visits.append(this_passcard_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    
    return render(request, 'passcard_info.html', context)
