from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


# After serializers and models were created, we doing ViewSets
class UserViewSet(viewsets.ModelViewSet):
    """

    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """

    API endpoint that allows group to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
