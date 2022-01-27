from django.shortcuts import render
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView,\
    UpdateAPIView
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import UserRegistrationSerializer, LoginSerializer

from django.contrib.auth import login, logout, authenticate

# This is User API registeration View for new user registeration for both examiner and examinee


class UserRegistrationView(CreateAPIView):
    """
    This API will be used to allow the users to SignUp for the WebApp.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    # def post(self, request, *args):
    #     new_user_serializer = UserRegistrationSerializer(data=request.data)
    #     if new_user_serializer.is_valid():
    #         new_user = new_user_serializer.create(request.data)
    #         # after getting the new user we need to create a user profile for him
    #         UserProfile.objects.create(
    #             user=User.objects.get(id=new_user.get('id')),
    #             device_id=request.data.get('device_id'),
    #             first_login=False
    #         )
    #         if new_user:
    #             return Response(
    #                 data={
    #                     "data": new_user,
    #                     "success": True
    #                 }, status=status.HTTP_201_CREATED
    #             )
    #     return Response(
    #         data={
    #             "message": list(new_user_serializer.errors.values())[0][0],
    #             "success": False
    #         }, status=status.HTTP_400_BAD_REQUEST
    #     )

# this is login API View for User login


class UserLoginView(CreateAPIView):
    """ 
    This API is for Logging in the this ONLINE TEST API
    """
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        user = authenticate(
            request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            return Response({"Logged in": "User Logged in"}, status=201)
        else:
            return Response({"Access denied": "User credential are incorrect"}, status=401)


# this is logout API view for User logging out.
class UserLogoutView(ListAPIView):
    """ 
    This API is Just a URL link but just by going through this user can Logout.
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"Logging out": "User Logged out."})
