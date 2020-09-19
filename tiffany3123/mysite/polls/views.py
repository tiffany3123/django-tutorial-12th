from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.views import generic
from django.http import Http404

# Create your views here.
#def detail(request, question_id):
 #   try:
  #      question = Question.objects.get(pk=question_id)
   # except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:7] #데이터 베이스에서 데이터를 가져옴
    context = {'latest_question_list': latest_question_list} #html에 넘겨주기 위해 하나의 dictionary 로 만
    return render(request, 'polls/index.html', context) #그거를 html 에 넘겨줌