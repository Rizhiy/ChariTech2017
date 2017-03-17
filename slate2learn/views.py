import calendar
import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from graphos.renderers.gchart import BarChart, LineChart, ColumnChart, PieChart
from graphos.sources.model import ModelDataSource
from graphos.sources.simple import SimpleDataSource

from slate2learn import EXPERIENCES, LEARNERS, TRANSACTIONS
from .models import Learner, Experience, Centre, Transaction
from django.db.transaction import atomic


# Create your views here.

def profile(request, pk):
    return HttpResponse("Profile {}".format(pk))


def centre_view(request, pk):
    template = 'slate2learn/centre.html'
    centre = Centre.objects.get(pk=pk)
    learners = centre.learner_set.all()
    monthly_income = centre.get_monthly_income()
    data_source = SimpleDataSource(monthly_income)
    income_chart = LineChart(data_source, options={'title': 'Monthly Income', 'legend': 'none','width':'100%'})
    context = {'centre': centre,
               'learners': learners,
               'conversion': centre.get_conversion_rate(),
               'income': centre.get_income(),
               'active_students': centre.get_active_students(),
               'attrition': centre.get_attrition_rate(),
               'income_chart': income_chart
               }
    return render(request, template, context)


def centre_learners(request):
    template = 'slate2learn/centre_chart.html'
    data_source = ModelDataSource(Centre.objects.all(), fields=['str_id', 'num_of_students'])
    chart = PieChart(data_source)
    context = {'chart': chart}
    return render(request, template, context)


def centre_join_rate(request, pk):
    template = 'slate2learn/centre_chart.html'
    year = datetime.datetime.today().year - 1
    month = datetime.datetime.today().month
    learners = [['Month', 'Number Of New Learners']]
    for i in range(0, 12):
        new_learners = len(centre_new_learners_in_month(pk, year, month))
        learners.append(["{} {}".format(calendar.month_name[month], year), new_learners])
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    data_source = SimpleDataSource(learners)
    chart = ColumnChart(data_source, options={'title': 'Join Rate', 'legend': 'none'})
    context = {'chart': chart}
    return render(request, template, context)


def centre_new_learners_in_month(centre_id, year, month):
    centre = Centre.objects.get(pk=centre_id)
    start_of_month = datetime.date(year=year, month=month, day=1)
    end_of_month = start_of_month + datetime.timedelta(days=30)
    learners = centre.learner_set.all().filter(date_joined__range=[start_of_month, end_of_month])
    return learners


def repopulate_db(request):
    Centre.objects.all().delete()
    Learner.objects.all().delete()
    Experience.objects.all().delete()
    Transaction.objects.all().delete()

    with atomic():
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
    return redirect("/")
