from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.urls import reverse
from .models import Marks,Marks1
def sample(request):
    credit=0
    product=0
    gpa=0
    all=Marks.objects.all().values()
    for i in all:
        product+=i['credit']*i['score']
        credit+=i['credit']
        gpa=round(product/credit,4)
    template=loader.get_template('intro.html')
    context={
        'all':all,
        'gpa':gpa,
       
    }
    return HttpResponse(template.render(context,request))
def homeRe(request):
    return redirect('/calc')
def fetch(request):
    creditt=request.POST['credit']
    scoree=request.POST['score']
    s1=Marks(credit=creditt,score=scoree)

    s1.save()
    return HttpResponseRedirect(reverse('sample'))
def delete(request,id):
    new=Marks.objects.get(id=id)
    new.delete()
    return HttpResponseRedirect(reverse('sample'))
def sample2(request):
    all1=Marks1.objects.all().values()
    
    summ=0
    c=0
    cgpa=0
    for i in all1:
        summ+=i['gpa']
        c+=1
    if summ:
        cgpa=round(summ/c,4)
    template=loader.get_template('cgpa.html')
    context={
        'all1':all1,
        'cgpa':cgpa,
    }
    return HttpResponse(template.render(context,request))
def fetchh(request):
    gscore=request.POST['gpa']
    t1=Marks1(gpa=gscore)
    t1.save()
    return HttpResponseRedirect(reverse('sample2'))
def deletee(request,id):
    new=Marks1.objects.get(id=id)
    new.delete()
    return HttpResponseRedirect(reverse('sample2'))
def revert(request):
    template=loader.get_template('intro.html')
    return HttpResponseRedirect(reverse('sample'))




