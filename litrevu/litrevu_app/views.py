from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Billet

class BilletCreateView(CreateView):
    model = Billet
    fields = ['title', 'description', 'image']
    template_name = 'litrevu_app/billet_form.html'
    success_url = reverse_lazy('litrevu_app:flux')

class HomeView(TemplateView):
    template_name = "litrevu_app/home.html"