# Create your views here.
from models import SharedSite
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, render
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf



@csrf_protect
def showGroupHarvard(request):
    i = request.META['REMOTE_ADDR']
    url_list = SharedSite.objects.all().filter(ip=i).order_by('-pk')[:30]
               
    try:
        bookmark = request.GET['name']
    except(Exception):
        bookmark = ''
    return render(request,'harvard_page_list.html',{'url_list':url_list,'bookmark':bookmark})

def showGroupCorkboard(request):
    i = request.META['REMOTE_ADDR']
    url_list = SharedSite.objects.all().filter(ip=i).order_by('-pk')[:30]
               
    try:
        bookmark = request.GET['name']
    except(Exception):
        bookmark = ''
    return render_to_response('corkboard_page_list.html',{'url_list':url_list,'bookmark':bookmark})

def add(request):
    return render_to_response('success.html')

@csrf_protect
def confirm(request):
    if request.method == 'POST':
        title = request.POST['title']
        usr = request.POST['user']
        url = request.POST['url']
        addr = request.META['REMOTE_ADDR']
        newEntry = SharedSite(title=title, url=url, user=usr, ip = addr)
        newEntry.save()
        return render_to_response('success.html')
    else:
        c = {}
        c['title'] = request.GET['title']
        c['user'] = request.GET['user']
        c['url'] = request.GET['url']
        return render(request,'confirm.html',c)
    
def home(request):
    i = request.META['REMOTE_ADDR']
    url_list = SharedSite.objects.all().filter(ip=i).order_by('-pk')[:30]
    try:
        bookmark = request.GET['name']
    except(Exception):
        bookmark = ''
    return render(request,'sidebar.html',{'url_list':url_list,'bookmark':bookmark})













