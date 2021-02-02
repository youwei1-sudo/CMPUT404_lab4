

from django.urls import path

from . import views

# THis is mysite/polls/url.py
# part1


# urlpatterns = [
#   path('', views.index, name='index')
# ]

# #part3
# urlpatterns = [
#     #'http://127.0.0.1/8000/polls/'
#     path('', views.index, name='index'),  #'http://127.0.0.1/8000/polls/' + ''
#     #'http://127.0.0.1/8000/polls/' + '5/'
#     # path('<str:question_id>/', views.detail, name='detail')
#     path('<int:question_id>/', views.detail, name='detail'),
#     # 'http://127.0.0.1/8000/polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # 'http://127.0.0.1/8000/polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# part 4
from django.urls import path

from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]