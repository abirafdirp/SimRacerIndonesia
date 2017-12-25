from django.shortcuts import render
from django.views.generic import TemplateView


class CalendarTemplateView(TemplateView):
    template_name = 'calendar.html'


class ResultsTemplateView(TemplateView):
    template_name = 'results.html'


class SeriesTemplateView(TemplateView):
    template_name = 'series.html'
