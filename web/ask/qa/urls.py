from django.conf.urls import url
from qa.views import quest, popularQuestions

urlpatterns = [
    url(r'^(?P<num>\d+)/$', quest),
]