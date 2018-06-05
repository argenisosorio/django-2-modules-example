# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Class that shows the index template of the start module.
    """
    template_name = "start/index.html"