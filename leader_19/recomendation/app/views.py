from django.template import loader
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, Http404, get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout

from .models import Question, Choice, UserId, Profile
from .forms import AnswerForm


def home(request):
	return render(request, 'app/home.html')

def catalog(request):
	return render(request, 'app/catalog.html')

def search(request):
	return render(request, 'app/search.html')

def results(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ('Ожидайте ответа...')
    else:
        form = AnswerForm()
    return render(request, 'app/results.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })

    
def vote(request, id):
    question_list = Question.objects.all()
    for question in question_list:

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist): 
            return render(request, 'app/test.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
        })
        else:
            selected_choice.votes += int (request.GET['votes'])
            selected_choice.save()
    return HttpResponseRedirect(reverse('app:results'))


def test(request):
    choice = Choice.objects.all()
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 1)
    page = request.GET.get('page')

    try:
        question = paginator.page(page)
    except PageNotAnInteger:
        question = paginator.page(1)
    except EmptyPage:
        question = paginator.page(paginator.num_pages)
    return render(request, 'app/test.html', {'question': question, 'page': page, 'choice': choice})
