from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime, timedelta
import time
# Create your views here.
from .forms import ReadingForm
from .models import Read, Tags


def read_list(request):
    blog_reads = Read.objects.all().order_by('-created_date')

    paginator = Paginator(blog_reads, 10)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    print type(blogs)
    return render(request, 'read_list.html', {'blogs_read': blogs})


    # t = get_template("read_list.html")
    # html = t.render()
    # return HttpResponse(html)


def read_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReadingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            blog_read = form.save(commit=False)
            blog_read.created_date = datetime.now()
            blog_read.save()

            k = set()
            for a in form.data['tags'].split(','):
                k.add(a.strip())
            for a in k:
                t, created = Tags.objects.get_or_create(tag=a)
                if not created:
                    t.tag = a
                    t.save()

                blog_read.tags.add(t)
            # blog_read.save()

            return render(request, 'reading_form.html', {'form': form, 'success': True})
        else:
            return render(request, 'reading_form.html', {'form': form, 'success': False})
            # if a GET (or any other method) we'll create a blank form
    else:
        form = ReadingForm()

    return render(request, 'reading_form.html', {'form': form})


def read_detail(request, id):
    r = Read.objects.get(id=id)
    # print r
    # TODO : figure out how to use dictionary here
    k = dict()
    k['content'] = r.data
    k['title'] = r.title
    k['url'] = r.url
    # print k['url']
    # return JsonResponse(data)
    return render(request, 'read_detail.html', k)


# TODO: Fix heatmap (i think it is fixed)

def heatmap_data(request):
    k = {'dhruv': 'dhruv'}
    blog_reads = Read.objects.values_list('created_date')
    l = {}
    for idx, a in enumerate(blog_reads):
        l[time.mktime(a[0].timetuple()) + idx] = 1
    return JsonResponse(l)


def write_form(request):
    return render(request, 'write_form.html')
