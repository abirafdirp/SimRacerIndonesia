from django.shortcuts import render
from django.views.generic import TemplateView


class CalendarTemplateView(TemplateView):
    template_name = 'calendar.html'

