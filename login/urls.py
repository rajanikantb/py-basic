from django.urls import path

from . import views

"""
# ex: /login/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
"""
app_name = 'login'
urlpatterns = [
    path('', views.index, name='index'),
]