

# THis is mysite/polls/url.py
# http//

from django.urls import path

from . import views

urlpatterns = [
    #'http://127.0.0.1/8000/polls/'
    path('', views.index, name='index'),  #'http://127.0.0.1/8000/polls/' + ''
    #'http://127.0.0.1/8000/polls/' + '5/'
    path('<int:question_id>/', views.detail, name='detail'),
    # 'http://127.0.0.1/8000/polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 'http://127.0.0.1/8000/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]