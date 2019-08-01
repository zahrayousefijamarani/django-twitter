from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404


def index(request):
    all_question = Question.objects.all()
    template = loader.get_template('./polls/index.html')
    context = {
        'all_question': all_question,
    }
    return HttpResponse(template.render(context, request))
    # return render(request,'',context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("there is nothing")
    return render(request, './polls/detail.html', context={'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, './polls/resualt.html', context={
        'question': question
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
