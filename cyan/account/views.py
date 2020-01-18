from django import views
from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import (
    render, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from account.utils import authcode

# 用户登录视图类
class Login(views.View):
    def get(self, request):
        print("get")
        data = "asfaf"
        return HttpResponse(data)


    def post(self, request):
        data = {}
        return HttpResponse(data)

            
            
# 验证码视图类
class GetAuthImg(views.View):
    """获取验证码视图类"""

    def get(self, request):
        data = authcode.get_authcode_img(request)
        print("验证码：",request.session.get("authcode"))
        return HttpResponse(data)