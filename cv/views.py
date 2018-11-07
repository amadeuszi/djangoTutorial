from django.shortcuts import render, redirect

from cv.models import Penalty


def create_users():
    user1 = Penalty.objects.all().filter(id = 1)
    user1 = list(user1)
    if len(user1) == 0:
        marlena = Penalty()
        amadeusz = Penalty()
        marlena.save()
        amadeusz.save()


def get_context():
    marlena = Penalty.objects.all().filter(id = 1)
    amadeusz = Penalty.objects.all().filter(id = 2)
    context = {}
    context['marlena_penalty'] = marlena[0].penalty
    context['amadeusz_penalty'] = amadeusz[0].penalty
    return context

def home(request):
    return render(request, 'cv/home.html')

def fund(request):
    create_users()
    return render(request, 'cv/fund.html', get_context())


def up(request, id):
    create_users()
    if request.method == 'POST':
        user1 = Penalty.objects.all().filter(id=id)[0]
        user1.penalty = user1.penalty + 1
        user1.save()
        return redirect('fund')


def down(request, id):
    create_users()
    if request.method == 'POST':
        user1 = Penalty.objects.all().filter(id=id)[0]
        user1.penalty = user1.penalty - 1
        user1.save()
        return redirect('fund')
