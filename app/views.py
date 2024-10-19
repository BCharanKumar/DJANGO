from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def example(request):
    #Here I am taking HttpRequest and I am returning HttpResponse
    return HttpResponse(' i am from views ')
def first(request):
    #Here I am taking HttpRequest and I am returning HTML Page
    return render(request,'first.html')

def insert_topic(request):
    tn=input('enter your topic_name!..')
    #TO=Topic(topic_name='CRICKET')
    #TO.save()
    #TO=Topic.objects.create(topic_name=tn)
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:

       

        return HttpResponse('OBJECT CREATED SUCCESSFULLY')
    else:
        return HttpResponse('is already exists')   
    
def insert_webpage(request):
    tn=input('enter your topic_name..!')
    n=input('enter your name..!')
    u=input('enter your url here..!')
    e=input('enter your email now..!')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
   
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)
    if WO[1]:
        return HttpResponse('The Object created successfully')
    else:
        return HttpResponse('That Object is already Exists')
    

def insert_accessrecord(request):
    tn=input('enter ur topic_name:')
    n=input('enter ur name:')
    u=input('enter ur url;')
    e=input('enter email..')
    a=input('enter ur author:!')
    d=input('enter the date!')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AO[1]:
         
         return HttpResponse('Object created successfully')
    else:
        return HttpResponse('is already we have bro!!!!')

def data_display(request):
    topics=Topic.objects.all()
    webpages=WebPage.objects.all()
    access=AccessRecord.objects.all()

    data={'topics':topics,'webpages':webpages,'access':access}
    return render(request,'display_data.html',data)