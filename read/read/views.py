from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, JsonResponse
from datetime import datetime, timedelta

def helloWorld(request):
    t = get_template('dashboard.html')
    html = t.render()

    return HttpResponse(html)
    # return HttpResponse("hello world")



def timePlus(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    now = datetime.now()
    html = 'It is currently %s' % now
    html += '<br>'
    later = now + timedelta(hours=offset)
    html += 'adding %s to %s is %s' % (offset, now, later)
    return HttpResponse(html)


def time(request):
    now = datetime.now()
    now = now + timedelta(hours=5.5)
    t = get_template('current_time.html')
    html = t.render(Context({'time': now}))

    return HttpResponse(html)
