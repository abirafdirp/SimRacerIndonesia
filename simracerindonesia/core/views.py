from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView

from simracerindonesia.users.models import UserProfile
from simracerindonesia.utils import get_page_range_helper_context


class CalendarTemplateView(TemplateView):
    template_name = 'calendar.html'


class ResultsTemplateView(TemplateView):
    template_name = 'results.html'


class SeriesTemplateView(TemplateView):
    template_name = 'series.html'


class SimRacersTemplateView(TemplateView):
    template_name = 'sim_racers.html'

    def get_context_data(self, **kwargs):
        sim_racers = UserProfile.objects.filter(user__is_staff=False)
        paginator = Paginator(sim_racers, 18)
        page = self.request.GET.get('page')

        for sim_racer in sim_racers:
            sim_racer.racing_simulators_trimmed = sim_racer.racing_simulators.all()[:3]
            sim_racer.racing_simulators_more = sim_racer.racing_simulators.all().count() - len(sim_racer.racing_simulators_trimmed)

        try:
            paginated_sim_racers = paginator.page(page)
        except PageNotAnInteger:
            paginated_sim_racers = paginator.page(1)
        except EmptyPage:
            paginated_sim_racers = paginator.page(paginator.num_pages)

        page_range_ctx = get_page_range_helper_context(
            paginator=paginator,
            paginated_object_list=paginated_sim_racers
        )

        ctx = {
            'paginated_sim_racers': paginated_sim_racers,
            **page_range_ctx,
            **super().get_context_data(**kwargs)
        }
        return ctx
