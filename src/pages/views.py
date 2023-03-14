from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
# from django.http import HttpResponse
from . models import Page

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/main.html', context)

def jupiter(request, pagename='jupiter'):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/jupiter.html', context)

def earth(request, pagename='earth'):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/earth.html', context)

def mercury(request, pagename='mercury'):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/mercury.html', context)

def venus(request, pagename='venus'):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/venus.html', context)

def mars(request, pagename='mars'):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    # assert False
    title = pg.title
    bodytxt = pg.bodytext
    context = {
        'title': title,
        'content': bodytxt,  # note the end-of-line comma
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/mars.html', context)
