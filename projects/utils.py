from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projectList = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projectList, search_query

def paginateQuerysets(request, querysets, results):

    page = request.GET.get('page')
    results = results
    paginator = Paginator(querysets, results)
    num_pages = paginator.num_pages

    try:
        querysets = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        querysets = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        querysets = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custome_range = range(leftIndex, rightIndex + 1)

    return querysets, custome_range, num_pages

