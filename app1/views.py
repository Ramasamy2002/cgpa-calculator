from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Marks, Marks1

def sample(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.save()  # Save session explicitly to generate a session key
        session_id = request.session.session_key
        print("Generated session ID:", session_id)
    else:
        print("Existing session ID:", session_id)

    credit = 0
    product = 0
    gpa = 0
    all_marks = Marks.objects.filter(session_id=session_id).values()
    print(all_marks)
    for i in all_marks:
        product += i['credit'] * i['score']
        credit += i['credit']
        gpa = round(product / credit, 4)

    template = loader.get_template('intro.html')
    context = {
        'all': all_marks,
        'gpa': gpa,
    }
    return HttpResponse(template.render(context, request))

def fetch(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.save()
        session_id = request.session.session_key
        print("Generated session ID:", session_id)
    else:
        print("Existing session ID:", session_id)

    creditt = request.POST['credit']
    scoree = request.POST['score']
    t = Marks(session_id=session_id, credit=creditt, score=scoree)
    t.save()

    return HttpResponseRedirect(reverse('sample'))

def delete(request, id):
    session_id = request.session.session_key
    Marks.objects.filter(id=id, session_id=session_id).delete()
    return HttpResponseRedirect(reverse('sample'))

def sample2(request):
    session_id = request.session.session_key
    all_marks1 = Marks1.objects.filter(session_id=session_id).values()

    summ = 0
    c = 0
    cgpa = 0
    for i in all_marks1:
        summ += i['gpa']
        c += 1

    if summ:
        cgpa = round(summ / c, 4)

    template = loader.get_template('cgpa.html')
    context = {
        'all1': all_marks1,
        'cgpa': cgpa,
    }
    return HttpResponse(template.render(context, request))

def fetchh(request):
    session_id = request.session.session_key
    gscore = request.POST['gpa']
    Marks1.objects.create(session_id=session_id, gpa=gscore)
    return HttpResponseRedirect(reverse('sample2'))

def deletee(request, id):
    session_id = request.session.session_key
    Marks1.objects.filter(id=id, session_id=session_id).delete()
    return HttpResponseRedirect(reverse('sample2'))

def revert(request):
    template = loader.get_template('intro.html')
    return HttpResponseRedirect(reverse('sample'))

def homeRe(request):
    if not request.session.session_key:
        request.session.save()
    return redirect('/calc')
