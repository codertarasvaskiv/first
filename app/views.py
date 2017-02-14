from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count, Max
from .models import Number, TimeDate
import datetime


def index(request):
    # number = Number.objects.get(number=3)
    # timed = TimeDate()
    # timed.time = timezone.now()
    # timed.number_id = number
    # timed.save()
    #
    # numbers = Number.objects.all()
    # for num in numbers:
    #     print(num)

    number = Number.objects.annotate(max_time=Max('timedate')).order_by('max_time').reverse()
    for n in number:
        print(n, n.timedate_set.count())
        print(list(n.timedate_set.all())[-1])





    numbers = Number.objects.all()
    times = TimeDate.objects.all()
    print('numbers' + str(numbers.count()))
    print('times' + str(times.count()))



    return render(request, 'index.html')
