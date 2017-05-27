from django.conf.urls import url
from . import views
from django.http import HttpResponse
from .models import Question

#urlpatterns=[
	# example: /polls/
#	url(r'^$', views.index, name='index'),

	#added the word 'specifics'
#	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#	# example: /polls/2/results/
#	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, #name='results'),
#	# example: /polls/2/vote/
#	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, #name='vote'),
#]"""

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	output= ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	
app_name = 'polls'
urlpatterns = [
	url(r'^$',views.IndexView.as_view(),name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

