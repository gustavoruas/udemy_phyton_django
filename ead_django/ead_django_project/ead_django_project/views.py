from django.views.generic import TemplateView

# Needed to force login into accessing URLS
from django.contrib.auth.decorators import login_required  #for Function based Views
from django.contrib.auth.mixins import LoginRequiredMixin  #for Class based Views

class IndexPage(LoginRequiredMixin, TemplateView):
    template_name = "index.html"