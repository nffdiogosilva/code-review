# How I would write the module views:
# August 12, 2019
# Nuno Diogo da Silva (diogosilva.nuno@gmail.com)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # I'm adding the permission_classes variable so that all actions of this viewset
    # can only be performed if the user is authenticated.
    permission_classes = [IsAuthenticated]

    # I could just add the permission 'IsAuthenticated' specifically to the action 'create' like this:
    #def get_permissions(self):
    #    """
    #    Instantiates and returns the list of permissions that this view requires.
    #    """
    #    if self.action == 'create':
    #        permission_classes = [IsAuthenticated]
    #    return [permission() for permission in permission_classes]

    # No need to override the 'create' action method since no special behavior is needed.
    # Reading the default create action implementation you can see that already handles the object creation.
    # This is the default implementation of the action 'create' (it's enough to validate and save the object):
    #def create(self, request, *args, **kwargs):
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #    self.perform_create(serializer)
    #    headers = self.get_success_headers(serializer.data)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
