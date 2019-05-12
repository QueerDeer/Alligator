from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class PodcastView(TemplateView):
    template_name = "podcast.html"


class PodcastDetailView(TemplateView):
    template_name = "podcast-detail.html"