from django.conf.urls import url,include
from account.views import Login, GetAuthImg

urlpatterns = [
    # 用户登录url
    url(r'^login/', Login.as_view(), name="login"),
    # 验证码url
    url(r'^get_auth_img/', GetAuthImg.as_view(), name="get_auth_img"),
]