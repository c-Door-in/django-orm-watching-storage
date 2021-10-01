from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .models import get_duration, format_duration


def storage_information_view(request):
    # Программируем здесь
    
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at=None)
    for active_visit in active_visits:
        duration = get_duration(active_visit)
        non_closed_visit = {
            'who_entered': active_visit.passcard.owner_name,
            'entered_at': active_visit.entered_at,
            'duration': format_duration(duration),
        }
        non_closed_visits.append(non_closed_visit)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
