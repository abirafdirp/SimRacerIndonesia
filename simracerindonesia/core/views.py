from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import TemplateView

from simracerindonesia.users.models import UserProfile
from simracerindonesia.utils import get_page_range_helper_context


class CalendarTemplateView(TemplateView):
    template_name = 'calendar.html'


class ResultsTemplateView(TemplateView):
    template_name = 'results.html'


class SeriesTemplateView(TemplateView):
    template_name = 'series.html'


class DriversTemplateView(TemplateView):
    template_name = 'drivers.html'

    def get_context_data(self, **kwargs):
        drivers = UserProfile.objects.all()
        paginator = Paginator(drivers, 30)
        page = self.request.GET.get('page')

        try:
            paginated_drivers = paginator.page(page)
        except PageNotAnInteger:
            paginated_drivers = paginator.page(1)
        except EmptyPage:
            paginated_drivers = paginator.page(paginator.num_pages)

        page_range_ctx = get_page_range_helper_context(
            paginator=paginator,
            paginated_object_list=paginated_drivers
        )

        ctx = {
            'paginated_drivers': paginated_drivers,
            **page_range_ctx,
            **super().get_context_data(**kwargs)
        }
        return ctx
