# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Class that shows the index template of the users module.
    """
    template_name = "users/index.html"