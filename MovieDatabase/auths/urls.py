from django.conf.urls import url
from auths.views import UserLoginView, UserRegisterView, UserLogoutView


urlpatterns = [
    url(r'^login/$', UserLoginView.as_view()),
    url(r'^logout/$', UserLogoutView.as_view()),
    url(r'^register/$', UserRegisterView.as_view()),
]
