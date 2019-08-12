# My Code Review of this module:
# August 12, 2019
# Nuno Diogo da Silva (diogosilva.nuno@gmail.com)

# Notes:
# Every comment made will be related to the code statement/snippet bellow it.

# Imports should be grouped in the following order:
# - Standard library imports.
# - Related third party imports.
# - Local application/library specific imports.
# You should put a blank line between each group of imports.
# For more information, please refer to PEP-8 (Style guide for python): https://www.python.org/dev/peps/pep-0008/#imports
from dateutil.relativedelta import relativedelta
from rest_framework import viewsets
# Wildcard imports (from <module> import *) should be avoided,
# as they make it unclear which names are present in the namespace,
# confusing both readers and many automated tools. 
# For more information, please refer to PEP-8 (Style guide for python): https://www.python.org/dev/peps/pep-0008/#imports
from rest_framework.response import *
import json


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Since a ModelViewset is being used, this 'action' should be a method of the class and not a top level function.
# For that, it needs to be indent 4 spaces (For more information, please refer to: https://www.django-rest-framework.org/api-guide/viewsets/)
def create(self, request):
        # This authentication validation, regarding code redability, and taking into account the SRP (Single Responsability Principle),
        # should be available through a function decorator, or in this case, in the permission_classes list, bellow the queryset option,
        #  taking advantage of the 'permissions' logic already given by
        # Django Rest Framework (please refer to: https://www.django-rest-framework.org/api-guide/permissions/#permissions)
        # i.e.: permission_classes = [IsAuthenticated]
        # Using the permission_classes list above would assure that a rightful response would be given,
        # with a correct status code returned. In this case,
        # the right one would be: 401 (assuming the highest priority authentication class does use WWW-Authenticate headers)
        # For more information, please refer to: https://www.django-rest-framework.org/api-guide/permissions/#how-permissions-are-determined
        if not request.user.is_authenticated():
            # As I already hinted in the above statement, this Response object is not returning the correct status code,
            # given the current situation. In this case, the right status code would be: 401 (for the reasons I've already wrote in the above comment)
            return Response("You should be authenticated")
        serializer = UserSerializer(data=request.data)
        # Since the 'is_valid' method raises an exception, due to the kwarg 'raise_exception=True',
        # if the data is invalid, this means that it will never go to the else statement instructions bellow,
        # because it will be "(...) dealt by the default exception handler that REST framework provides,
        # and will return HTTP 400 Bad Request responses by default".
        # (for more information, please refer to: https://www.django-rest-framework.org/api-guide/serializers/#raising-an-exception-on-invalid-data)
        if serializer.is_valid(raise_exception=True):
            # The comment data should be accessed through the serializer validation object,
            # and not directly through the 'http_method' object ('request.POST').
            # This way, we're making sure that we're accessing the comment object after its validation
            # and not the other way around.
            # The right way to access it would be: serializer.validated_data["comment"]
            comment = request.POST["comment"]
            # This code here it's not respecting the SRP (Single Responsability Principle) convention.
            # The object creation logic should live in another place and not inside the view.
            # Please refer to: https://en.wikipedia.org/wiki/Single_responsibility_principle
            # Also, this object creation is responsability of the UserSerializer object.
            # small note: For good practice, use all double quotes or just simple quotes. 
            # Example: comment = request.POST["comment"]; serializer.validated_data['email']
            user = User.objects.create(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                comment=comment,
            # Assuming that the object was successfully created, 
            # the response status code should be 201 and not 200.
            # By having a 201 status code it's not necessary to send a variable called 'success' in the response context,
            # since the status code itself confirms its success.
            # For more information, please refer to: https://httpstatuses.com/201
            response = {'code': 200, 'success': True, 'id': user.id}
            return Response(response)
        else:
            # Print statements can be helpful while developing/debugging
            # (I'd prefer pdb library: https://docs.python.org/3/library/pdb.html or django runserver command (with print function)),
            # but they should not be committed into the repository.
            # If we want to log a runtime error or a warning, we should do it using the native python module logging.
            # i.e: (import logging; logger = logging.getLogger(__name__); logger.error("User not created!"))
            print ('error on the creation')
            # This return statement returns a response that by default has a 200 status code 
            # (for more information, please refer to: https://www.django-rest-framework.org/api-guide/responses/#creating-responses), 
            # implying that the request was successful.
            # Assuming that this code, inside the else statement, would run (for that to happen we would need to remove the flag 'raise_exception=True' from the method 'is_valid'),
            # the status code returned should be 400, since it would only run if the data was invalid.
            # By having a 400 status code it warns that the server cannot or will not process the request.
            # For more information, please refer to: https://httpstatuses.com/400
            return Response('error')