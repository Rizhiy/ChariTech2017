from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from slate2learn import EXPERIENCES, LEARNERS, TRANSACTIONS
from .models import Learner, Experience, Centre, Transaction


# Create your views here.

def profile(request, pk):
    return HttpResponse("Profile {}".format(pk))


def centre_view(request, pk):
    template = 'slate2learn/centre.html'
    centre = Centre.objects.get(pk=pk)
    learners = centre.learner_set.all()
    context = {'centre': centre, 'learners': learners, 'income': centre.income()}
    return render(request, template, context)


def repopulate_db(request):
    Centre.objects.all().delete()
    Learner.objects.all().delete()
    Experience.objects.all().delete()
    Transaction.objects.all().delete()

    for i in range(1, 4):
        c = Centre(id=i)
        c.save()

    for learner in LEARNERS:
        l = Learner(**learner)
        l.save()

    for experience in EXPERIENCES:
        e = Experience(**experience)
        e.save()

    for transaction in TRANSACTIONS:
        t = Transaction(**transaction)
        t.save()

    messages.success(request, "DB repopulated")
    return redirect("")
