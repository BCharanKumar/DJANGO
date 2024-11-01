from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.functions import Length


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
     #If we want to get all the data commonly we will use all
    topics=Topic.objects.all()
    webpages=WebPage.objects.all()
    access=AccessRecord.objects.all()

    data={'topics':topics,'webpages':webpages,'access':access}
    return render(request,'display_data.html',data)

def data_retriev(request):
    #If we want to get all the data commonly we will use 'all method '
    #topics=Topic.objects.all()
    #webpages=WebPage.objects.all()
    #access=AccessRecord.objects.all()
    
    #if we want to retriev the specific data we will go for 'get method '
    #print(WebPage.objects.get(name='CHARAN',url='https://cherry.in'))

    #but mostly or commomly when we r dealing with get we will use primary key column 
    #print(WebPage.objects.get(id=14))

    #If the get method condtion satisfies more than one row...
    #print(WebPage.objects.get(topic_name='CRICKET'))
    #Error is the answer becoz
    #if the get method statisfies multi rows it will return an error bcoz get method is able to satisfiy only one row
    
    # when we r inserting data into child table we should get the object of parent then in that case we will use get method to get that object
    '''
    tn=input('enter ur topic_name:')
    n=input('enter ur name:')
    u=input('enter ur url;')
    e=input('enter email..')
    a=input('enter ur author:!')
    d=input('enter the date!')

    TO=Topic.objects.get(topic_name=tn)
    WO=WebPage.objects.get(topic_name=TO,name=n,url=u)
    AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)
    if AO[1]: 
         return HttpResponse('Object created successfully')
    else:
        return HttpResponse('is already we have bro!!!!')
'''
    
    #If we want to retriev specific data we can use the filter method as well
    topics=Topic.objects.filter(topic_name='BOXING')

    #Using filter with & operator 
    webpages=WebPage.objects.filter(id=3,name='CHARAN')#we no need to use any other objects
    access=AccessRecord.objects.filter(author='CHERRY',id=8)#no rows satisfy no error no operation

    #If the filter method satisfies more than one row also it will display the values
    webpages=webpages=WebPage.objects.filter(topic_name='CRICKET')
     
    #Using filter with | operator here Q is mondatory
    webpages=webpages=WebPage.objects.filter(Q(topic_name='CRICKET') | Q(topic_name='BOXING'))
    #If u r not using Q error will accured
    access=AccessRecord.objects.filter(Q(author='ANUSHKA SHARMA') | Q(id=8))
    #By using exclude data retrieving 
    access=AccessRecord.objects.exclude(author__contains='A')
    webpages=webpages=WebPage.objects.exclude(name__startswith='R',email__contains='k')
    topics=Topic.objects.exclude(topic_name='CRICKET') 
    access=AccessRecord.objects.exclude(date__year__lt=1995,date__hour__lte=8)
    '''Simply the functionality of exclude is similar to filter but it will gives the output
      what r the rows conditions not satisfies given conditions(if condition satisfies that will not be there in output)'''

    data={'topics':topics,'webpages':webpages,'access':access}
    
    return render(request,'display_data.html',data)



def data_order(request):
    topics=Topic.objects.all()
    webpages=WebPage.objects.all()
    access=AccessRecord.objects.all()

    #Arranging the data in aascending order
    topics=Topic.objects.all().order_by('topic_name')
    webpages=WebPage.objects.all().order_by('name')
    access=AccessRecord.objects.all().order_by('author')

    #Arranging the data in discending order
    topics=Topic.objects.all().order_by('-topic_name')
    webpages=WebPage.objects.all().order_by('-url')
    access=AccessRecord.objects.all().order_by('-author')

    #Arranging the data in aascending order
    topics=Topic.objects.all().order_by(Length('topic_name'))
    webpages=WebPage.objects.all().order_by(Length('name'))
    access=AccessRecord.objects.all().order_by(Length('author'))

    #Arranging the data in discending order
    topics=Topic.objects.all().order_by(Length('topic_name').desc())
    webpages=WebPage.objects.all().order_by(Length('name').desc())
    access=AccessRecord.objects.all().order_by(Length('author').desc())



    data={'topics':topics,'webpages':webpages,'access':access}
    return render(request,'display_data.html',data)
    
def field_lookups(request):
    try:

        topics=Topic.objects.all()
        webpages=WebPage.objects.all()
        access=AccessRecord.objects.all()
        #Using of the field lookups 
        topics=Topic.objects.all().order_by(Length('topic_name')).filter(Q(topic_name__startswith='C') | Q(topic_name__endswith='l'))
        webpages=WebPage.objects.all().order_by(Length('name').desc()).filter(name__contains='A',name__startswith='H',name__endswith='A')
        access=AccessRecord.objects.all().order_by(Length('author').desc()).filter(Q(author__iregex=r'^a') | Q(author__iregex=r'u$') | Q(author__iregex=r'[i]'))
        webpages=WebPage.objects.filter(id__gt=5,pk__lte=19)
        access=AccessRecord.objects.filter(date__year__gte=2000,date__month__lte=6)
        access=AccessRecord.objects.filter(date__week__range=(1,25))
        access=AccessRecord.objects.filter(date__week__range=(25,50),date__week_day__range=(1,5))
        access=AccessRecord.objects.filter(Q(date__day=19) | Q(date__month__range=(3,9)))
        access=AccessRecord.objects.filter(pk__in=[1,10,2,7,3,9,4,5])
        access=AccessRecord.objects.filter(date__hour__gt=6,date__minute__range=(10,40))
        access=AccessRecord.objects.filter(Q(date__minute__in=[6,7,8,12,45,53,6,52]) | Q(date__second__in=[4,5,6,7,8,45,6,52]))
        access=AccessRecord.objects.filter(date__week_day__range=(5,17))
        
    except Exception as e:
        return HttpResponse(f"Error is: {e}")
        
    data={'topics':topics,'webpages':webpages,'access':access}
    return render(request,'display_data.html',data)


def sel_rel_method(request):
    topics=Topic.objects.all()
    webpages=WebPage.objects.all()
    access=AccessRecord.objects.all()

    
    LWO=WebPage.objects.select_related('topic_name').filter(topic_name='CRICKET')
    LWO=WebPage.objects.select_related('topic_name').filter(name__startswith='C',email__contains='')
    LWO=WebPage.objects.select_related('topic_name').filter(name__contains='R',id__gt=8)
    LWO=WebPage.objects.select_related('topic_name').filter(url__contains='e',name__iregex=r'^C').order_by('-email')
    LWO=WebPage.objects.select_related('topic_name').filter(Q(id=10) | Q(name__endswith='A')).order_by(Length('topic_name'))
    LWO=WebPage.objects.select_related('topic_name').filter(name__iregex=r'^C',email__contains='A')
    LWO=WebPage.objects.select_related('topic_name').filter(id__in=[1,3,7,9,8,4,13],name__endswith='A').order_by('name').order_by(Length('email'))
    LWO=WebPage.objects.select_related('topic_name').all()

    LAO=AccessRecord.objects.select_related('name').filter(date__year__lt=2000)
    LAO=AccessRecord.objects.select_related('name').filter(date__month__range=(2,7),author__contains='K')
    LAO=AccessRecord.objects.select_related('name').filter(author__contains='U').order_by('-id')
    LAO=AccessRecord.objects.select_related('name').filter(Q(id__gt=3) | Q(date__week__range=(2,30))).order_by(Length('author').desc())
    LAO=AccessRecord.objects.select_related('name').filter(name__email__contains='e')
    LAO=AccessRecord.objects.select_related('name').filter(Q(id__gt=8) | Q(name__url__contains='e'))
    LAO=AccessRecord.objects.select_related('name').filter(date__hour__range=(2,10),author__iregex=r'[A]')
    LAO=AccessRecord.objects.select_related('name').filter(date__minute__in=[1,6,56,34,59,13,45,36,23])
    LAO=AccessRecord.objects.select_related('name').filter(Q(id__lt=25) | Q(name__email__contains='e'),name__url__startswith='h').order_by('-name__email')
    LAO=AccessRecord.objects.select_related('name').filter(Q(name__url__iregex=r'n$') , Q(author__endswith='A') | Q(name__email__startswith='k')).order_by(Length('author'))
    LAO=AccessRecord.objects.select_related('name').filter(name__url__contains='l' , date__month__gte=6,date__year__lt=2015)
    LAO=AccessRecord.objects.select_related('name').all()

    data={'topics':topics,'webpages':webpages,'access':access,'LWO':LWO,'LAO':LAO}
    return render(request,'joins.html',data)

def prerecth_rel_method(request):
    LTWO=Topic.objects.prefetch_related('webpage_set').all()
    LTWO=Topic.objects.prefetch_related('webpage_set').filter(topic_name__contains='A')
    #LTWO=Topic.objects.prefetch_related('webpage_set').filter(webpage_set__name='MESSI')
    LTWO=Topic.objects.prefetch_related('webpage_set').exclude(topic_name='T BILLA',)
    LTWO=Topic.objects.prefetch_related('webpage_set').exclude()
    d={'LTWO':LTWO}

    return render(request,'prerecth_rel_method.html',d)




def dummy(request):
    return render(request,'dummy.html')
def home(request):
    return render(request,'home.html')
def alerts(request):
    return render(request,'alerts.html')
def buttons(request):
    return render(request,'buttons.html')

def badge(request):
    return render(request,'badge.html')

def forms(request):
    return render(request,'forms.html')
def dropdown(request):
    return render(request,'dropdown.html')


def buttongroup(request):
     return render(request,'buttongroup.html')
