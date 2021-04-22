from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

from app.models import Profile, Question, Comment, Tag
from app.forms import LoginForm, AskForm, SignupForm, CommentForm, SettingsForm, AvatarForm
from django.contrib import messages


def paginate(objects_list, request, per_page=5):
    limit = request.GET.get('limit', per_page)
    paginator = Paginator(objects_list, limit)
    page = request.GET.get('page')
    objects_page_list = paginator.get_page(page)
    return objects_page_list


def new_questions(request):

    db_question = Question.objects.newest()
    pag_questions = paginate(db_question, request)

    return render(request, 'new_questions.html', {
        'questions': pag_questions,
        'tags': Tag.objects.popular(),
        'best_members': Profile.objects.best()
    })
    
def hot_questions(request):

    db_question = Question.objects.hottest()
    pag_questions = paginate(db_question, request)

    return render(request, 'hot_questions.html', {
        'questions': pag_questions,
        'tags': Tag.objects.popular(),
        'best_members': Profile.objects.best()
    })
    
def tag_questions(request):

    pag_questions = paginate(questions, request)

    return render(request, 'tag_questions.html', {
        'questions': pag_questions,
        'tag': 'All tags',
        'tags': Tag.objects.popular(),
        'best_members': Profile.objects.best()
    })
    
    
def signin(request):
    next_page = request.GET.get('next', '/')
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)
            if user is not None:
                auth.login(request, user)
                print("\nFEFE\n")
                return redirect('/api/v1/')
        messages.error(request, 'Invalid username or password')
        print("\nKEKE\n")
        return redirect(next_page)


    return render(request, 'signin.html', {
        'tags': Tag.objects.popular(),
        'best_members': Profile.objects.best(),
        'form': form,
        'next': next_page
    })
