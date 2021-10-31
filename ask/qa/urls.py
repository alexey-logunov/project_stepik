"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('question/<int:pk>/', views.QuestionView.as_view(), name='question'),
    path('ask/', views.CreateQuestion.as_view(), name='question_add'),
    path('popular/', views.PopularView.as_view(), name='popular'),
    path('new/', views.MainView.as_view(), name='new'),
]

# urlpatterns = [
#     url(r'^', views.test, name='home'),
#     url(r'^login/', views.test, name='login'),
#     url(r'^signup/', views.test, name='signup'),
#     url(r'^question/<int:question_id>/', views.QuestionView.as_view(), name='question_details'),
#     url(r'^ask/', views.test, name='ask'),
#     url(r'^popular/', views.PopularView.as_view(), name='popular'),
#     url(r'^new/', views.MainView.as_view(), name='new')
# ]
