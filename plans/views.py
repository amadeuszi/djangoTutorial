import datetime
from datetime import timedelta

from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from plans.models import Schedule


def schedule_add(request):
    if request.method == 'POST':
        return schedule_add_post(request)
    else:
        return schedule_add_get(request)


def schedule_add_post(request):
    schedule = Schedule()
    schedule.day_date = datetime.datetime.strptime(request.POST.get('day_date'), "%m/%d/%Y").date()
    schedule.duration = timedelta(hours=float(request.POST.get('duration')))
    schedule.description = request.POST.get('description')
    schedule.save()
    return redirect(reverse('schedule_add') + '?date=' + schedule.day_date.strftime("%Y-%m-%d"))


def schedule_add_get(request):
    ctx = {}
    current_schedule_list = None
    if 'date' in request.GET:
        current_schedule_list = list(Schedule.objects.all().filter(day_date=request.GET.get('date')))
        date = datetime.datetime.strptime(request.GET.get('date'), "%Y-%m-%d").strftime("%m/%d/%Y")
    else:
        current_schedule_list = []
        date = ''
    ctx['current_schedule_list'] = current_schedule_list
    ctx['date'] = date
    return render(request, 'plans/schedule_add.html', ctx)