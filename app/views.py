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
    from django.db.models import Q
    #If we want to retriev specific data we can use the filter method as well
    topics=Topic.objects.filter(topic_name='BOXING')

    #Using filter with & operator 
    webpages=WebPage.objects.filter(id=3,name='CHARAN')#we no need to use any other objects
    access=AccessRecord.objects.filter(author='CHERRY',id=8)#no rows satisfy no error no operation

    #If the filter method satisfies more than one row also it will display the values
    webpages=webpages=WebPage.objects.filter(topic_name='CRICKET')
     
    #Using filter with | operator here Q is mondatory
    webpages=webpages=WebPage.objects.filter(Q(topic_name='CRICKET') | Q(topic_name='BOXING'))#If u r not using Q error will accured
    access=AccessRecord.objects.filter(Q(author='ANUSHKA SHARMA') | Q(id=8))
    #By using exclude data retrieving 
    access=AccessRecord.objects.exclude(author__contains='A')   
    webpages=webpages=WebPage.objects.exclude(name__startswith='A',email__contains='K',url__contains='l')
    access=AccessRecord.objects.exclude(date__year__lt=1995,date__hour__lte=8)
    '''Simply the functionality of exclude is similar to filter but it will gives the output
      what r the rows conditions not satisfies given conditions(if condition satisfies that will not be there in output)'''

 
    
    
    data={'topics':topics,'webpages':webpages,'access':access}
    
    return render(request,'display_data.html',data)
