from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # both name AND short_intro cantains S_Q    (&&)
    # profiles = Profile.objects.filter(name__icontains=search_query, short_intro__icontains=search_query)

    # skills = Skill.objects.filter(name__iexact=search_query)

    skills = Skill.objects.filter(name__icontains=search_query)
    # convert to || with django.db.models.Q
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                                 Q(short_intro__icontains=search_query) |
                                                 Q(skill__in=skills))
    return profiles, search_query
