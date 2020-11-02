from django.shortcuts import render
from rest_framework import viewsets,mixins
# Create your views here.
from rest_framework.response import Response
from app.models import User
from app.serializers import BookModelSerializer


class LoginViewSetView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = BookModelSerializer

    def user_login(self,request,*args,**kwargs):
        request_data = request.data
        username = request_data.get("username")
        password = request_data.get("password")
        res = User.objects.filter(username=username,password=password)
        serializer = BookModelSerializer(request_data).data
        if res:
            return Response({
                "status":200,
                "message":"登录成功",
                "results":serializer,
            })
        return Response({
            "status":400,
            "message":"登录失败",
        })


class RegisterViewSetView(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = BookModelSerializer

    def user_register(self,request,*args,**kwargs):
        request_data = request.data
        username = request_data.get("username")
        password = request_data.get("password")
        # print(username)
        # print(password)
        # print(request_data)
        res = User.objects.filter(username=username)
        if res:
            return Response({
                "status":400,
                "message":"用户名已存在",
            })
        serializer = BookModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        return Response({
            "status":200,
            "message":"注册成功",
            "results":BookModelSerializer(user_obj).data,
        })