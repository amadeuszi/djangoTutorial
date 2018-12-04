import datetime
from datetime import timedelta

from django.shortcuts import render, redirect

from cv.models import Penalty


def create_users():
    marlena = Penalty.objects.all().filter(id = 1)
    marlena = list(marlena)
    if len(marlena) == 0:
        marlena = Penalty()                 # Marlena = 1
        marlena.name = 'Marlena'
        amadeusz = Penalty()                # Amadeusz = 2
        amadeusz.name = "Amadeusz"
        nowak = Penalty()                   # Nowak = 3
        nowak.name = 'Nowak'
        angelika = Penalty()                # Angelika = 4
        angelika.name = 'Angelika'
        marlena.save()
        amadeusz.save()
        nowak.save()
        angelika.save()


def get_amadeusz():
    return Penalty.get(pk=2)


def get_angelika():
    return Penalty.get(pk=4)


def get_nowak():
    return Penalty.get(pk=3)


def get_marlena():
    return Penalty.get(pk=1)


def get_context():
    return {
        'users': list(Penalty.objects.all().filter(id__lte=2))
    }


def home(request):
    return render(request, 'cv/home.html')


def fund(request):
    create_users()
    return render(request, 'cv/fund.html', get_context())


def up(request):
    name = request.POST['name']
    penalty_name = request.POST['penalty_name']
    view_name = request.POST['view_name']
    create_users()
    if request.method == 'POST':
        user = Penalty.objects.get(name=name)
        if penalty_name == 'penalty':
            user.penalty += 1
        elif penalty_name == 'diet_strike':
            user.diet_strike += 1
        elif penalty_name == 'non_smoking_strike':
            user.non_smoking_strike += 1
        user.save()
        return redirect(view_name)


def down(request):
    name = request.POST['name']
    penalty_name = request.POST['penalty_name']
    view_name = request.POST['view_name']
    create_users()
    if request.method == 'POST':
        user = Penalty.objects.get(name=name)
        if penalty_name == 'penalty':
            user.penalty -= 1

        elif penalty_name == 'diet_strike':
            user.diet_strike -= 1
        elif penalty_name == 'non_smoking_strike':
            user.non_smoking_strike -= 1
        user.save()
        return redirect(view_name)


def get_ms(dt):
    return int(round(dt.timestamp() * 1000))

def get_dieting():
    return list(Penalty.objects.all().filter(pk__gte=2))


def get_start_date():
    return datetime.datetime.strptime('Dec 3 2018  1:00AM', '%b %d %Y %I:%M%p')


def get_now_date():
    return datetime.datetime.now()


def days_from_start():
    time_delta = timedelta(milliseconds=get_ms(get_now_date()) - get_ms(get_start_date()) + 1000 * 60 * 60 * 24)
    return time_delta.days


def diet(request):
    create_users()
    context = {
        'users': get_dieting(),
        'days_from_start': days_from_start(),
    }
    return render(request, 'cv/diet.html', context)








































