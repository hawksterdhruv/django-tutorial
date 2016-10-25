from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from datetime import datetime, timedelta
# Create your views here.
from .forms import ReadingForm


def read_list(request):
    t = get_template("read_list.html")
    html = t.render()
    return HttpResponse(html)


def read_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReadingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'reading_form.html', {'form': form, 'success':True})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ReadingForm()

    return render(request, 'reading_form.html', {'form': form})
