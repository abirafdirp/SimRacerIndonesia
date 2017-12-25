from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^calendar/$', views.CalendarTemplateView.as_view(), name='calendar'),
    url(r'^results/$', views.ResultsTemplateView.as_view(), name='results'),
    url(r'^series/$', views.SeriesTemplateView.as_view(), name='series'),
]
