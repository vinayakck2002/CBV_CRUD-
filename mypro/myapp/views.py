from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from . models import *
from django.urls import reverse_lazy


# Class One just return the without using templates
# Create your views here.
class CBView(View):
    def get(self,request):
        return HttpResponse("<h1> Welcome to Advance Django!!!")
# ======================================================================
  
# Class Two using template View
class CBTemplateView(TemplateView):
    template_name = 'index.html'

# Get contxt_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # as a correct situation context is dictionary
        context['value'] = "this is context data"
        return context
    
# Extra context_data
    extra_context = {'values':'this is the extra context'}
    #simple method but some limitation are their

# ======================================================================
class SchoolListView(ListView):
    context_object_name = 'schoolist'
    model = School
    template_name = 'SchoolList.html'

class SchoolDetailView(DetailView):
    context_object_name = 'schooldetail'
    model = School
    template_name ='SchoolDetail.html'

class SchoolCreateView(CreateView):
    fields = ('name','location')
    model = School
    template_name = 'SchoolForm.html'

class SchoolUpdateView(UpdateView):
    fields = ('name',)
    model = School
    template_name = 'SchoolForm.html'

class SchoolDeleteView(DeleteView):
    model = School
    #inbuild url success_url
    success_url = reverse_lazy('list')
    template_name = 'SchoolDelete.html'



