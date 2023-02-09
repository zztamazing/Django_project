from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},

    ]

    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    print('**********************************USER:', request.user)
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    # user = request.user.profile
    data = request.data
    print('--------------------------------------------------------DATA:', data)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


"""
23fall = $15322 + $816.17 = $16135.17
23winter = $15322 + $816.17 = $16135.17
24fall = $15322 + $816.17 + $800= $16935.17
24winter = $15322 + $816.17 +$800 = $16935.17          /        23winter = $7661 + $558.15 +$400 = $16935.17  

===>  $66140.68        /          $57824.66   in total

*22spring $15,392.95*
"""
