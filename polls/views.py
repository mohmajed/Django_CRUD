from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm, VacationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Successfully Created For ' + user)
            return redirect('polls:login')

    context = {'form':form}
    return render(request,'polls/register.html',context)

@unauthenticated_user
def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('polls:home')
        else:
            messages.info(request,'Username Or Password Were Incorrect ')

    context = {}
    return render(request,'polls/login.html',context)


def logout_user(request):
    logout(request)
    return redirect('polls:login')


@login_required(login_url='polls:login')
def home(request):
    user = request.user
    # get the user specific vacations this way (parent.childmodel_set.all())
    vacations = user.vacation_set.all()
    context = {'user':user, 'vacations':vacations}
    return render(request,'polls/home.html',context)


@login_required(login_url='polls:login')
def create_vacation(request):
    form = VacationForm()
    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            #automatically assign the employee id of the current user
            object = form.save(commit=False)
            user = request.user
            object.employee = request.user
            object.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'polls/vacation_form.html',context)


@login_required(login_url='polls:login')
def update_vacation(request,pk):
    vacation = Vacation.objects.get(id=pk)
    form = VacationForm(instance=vacation)

    if request.method == "POST":
        form = VacationForm(request.POST,instance=vacation)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'polls/vacation_form.html',context)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
