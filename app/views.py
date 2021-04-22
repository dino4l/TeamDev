from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

from app.models import Profile, Question

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