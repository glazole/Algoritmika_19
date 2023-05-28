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
   # question = get_object_or_404(Question, pk=question.id)
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
    return HttpResponseRedirect(reverse('app:results')) #, args=(id,)))

def test(request):
    choice = Choice.objects.all()
    question_list = Question.objects.all()
    #question_list = Question.objects.get_queryset().order_by('id')
    paginator = Paginator(question_list, 1)
    page = request.GET.get('page')

    try:
        question = paginator.page(page)
    except PageNotAnInteger:
        question = paginator.page(1)
    except EmptyPage:
        question = paginator.page(paginator.num_pages)
    return render(request, 'app/test.html', {'question': question, 'page': page, 'choice': choice})

    # if paginator.page(page) == 11:
   #     return HttpResponse ('votes') 

def test3(request):
    data={'form_':''}
    #   Если в сессии нет нужных переменных, то создаем
    if 'question' not in request.session:
        request.session['question']={}
        request.session['vote'] = 0
        index = 1
        for row in my_quests:
            request.session['question'][index]=None
            index +=1
        request.session.modified = True

    #   нам пришел ответ, то считаем его
    if 'vote' in request.GET:
        request.session['vote'] += int (request.GET['vote'])
        request.session['question'][request.GET['page']] = 'Done'
        request.session.modified = True
        print (request.session['vote'])

    if 'page' not in request.GET:
        return redirect ('/test/?page=1')
    else:
        #   Если был получен ответ на этот вопрос, то идем дальше
        if request.session['question'][request.GET['page']] != None:
            next_page = int(request.GET['page'])+1
            #   Если на все вопросы даны ответы, то возвращаем результат
            if next_page-1>=len(my_quests):
                return HttpResponse ('Вы завершили тестирование и набрали '+str(request.session['vote'])+' баллов!')
            return redirect ('/test/?page='+ str(next_page))
        else:
            #   Рендерим форму
            data['form_']=render_form (int(request.GET['page']))
    return render (request, 'index.html', data)


#    return render(request, 'app/test.html', {
 #   'question': question, 'page': page, 'choice': choice})


#   Переменная с вопросами и ответами/баллами
my_quests = {
    1:['Выберите любое число', ['Два', 0],['Семь', 1],['Восемь', 2]],
    2:['Выберите любой цвет', ['Красный', 0],['Желтый', 1],['Синий', 2]],
    3:['Выберите любое животное', ['Корова', 0],['Носорог', 1],['Жираф', 2]],
    4:['Выберите то, что нельзя выбрать', ['Можно выбрать', 0],['Нельзя выбрать', 1]],
    5:['Попробуйте ничего не выбрать', ['Выбрать', 0],['Не выбрать', 1]],
}

#   Отвечает за формирование элементов в форме
def render_form (number):
    choices = Choice.objects.all()
    questions = Question.objects.all()

    HTML_='<input name="page" value="'+str(number)+'" hidden><h3>'+ questsions[number]+'</h3>'
    for row in questions[number][1:len(queststions[number])]:
        HTML_+='<p>'+row[0]+' <input name="vote" value="'+str(row[1])+'" type="radio"></p>'
    return HTML_


