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
from .views import MainView, QuestionView, PopularView, CreateQuestion, SignUpView, SignInView, FeedBackView, \
    SuccessView, SearchResultsView
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('login/', SignInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('question/<int:pk>/', QuestionView.as_view(), name='question'),
    path('ask/', CreateQuestion.as_view(), name='question_add'),
    path('popular/', PopularView.as_view(), name='popular'),
    path('new/', MainView.as_view(), name='new'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
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
