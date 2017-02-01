from django.conf.urls import url
from qa.views import quest

urlpatterns = [
	url(r'^(?P<num>\d+)/$', quest),
]