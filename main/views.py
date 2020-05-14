from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MainView(TemplateView):
    template_name = 'main/home.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

