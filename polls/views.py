from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # Dictionary to pass data to the template
    context = {"latest_question_list": latest_question_list}
    
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # Get the question object or return a 404 error if not found
    question = get_object_or_404(Question, pk=question_id)
    
    # Render the detail template with the question object
    # The template will have access to the 'question' variable
    # and can display its attributes like question_text and pub_date
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."

    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)