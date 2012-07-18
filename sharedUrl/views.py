# Create your views here.
from models import SharedSite
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def showGroup(request):
    i = request.META['REMOTE_ADDR']
    url_list = SharedSite.objects.all().filter(ip=i).order_by('-pk')[:30]
    bookmark = ''
    try:
        bookmark = request.GET['name']
    except(Exception):
        bookmark = ''
    return render_to_response('page_list.html',{'url_list':url_list,'bookmark':bookmark})

def add(request):
    title1 = request.GET['title']
    usr = request.GET['user']
    url1 = request.GET['url'] 
    addr = request.META['REMOTE_ADDR']
    if title1:
        new_entry = SharedSite(title=title1, url=url1, user=usr, ip=addr)
        new_entry.save()
    else:
        new_entry = SharedSite(title=url1, url=url1, user=usr, ip=addr)
        new_entry.save()
    return render_to_response('success.html')