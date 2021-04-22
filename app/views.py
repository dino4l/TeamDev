from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def paginate(objects_list, request, per_page=5):
    limit = request.GET.get('limit', per_page)
    paginator = Paginator(objects_list, limit)
    page = request.GET.get('page')
    objects_page_list = paginator.get_page(page)
    return objects_page_list
