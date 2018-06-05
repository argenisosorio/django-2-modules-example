# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Class that shows the index template of the projects module.
    """
    template_name = "projects/index.html"