from django.shortcuts import render
from appe.models import EditingView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView



# Create your views here.
class AddNewEmployee(CreateView):
    model=EditingView
    template_name = 'newemployee.html'
    fields='idno','name','age','salary','contactno','email',
    success_url = '/index/'


class updateemployee(UpdateView):
    model = EditingView
    template_name = 'update.html'
    fields = 'idno','name','age','salary','contactno','email',
    success_url ='/viewall/'


class deleteemployee(DeleteView):
    model=EditingView
    template_name = 'delete.html'
    success_url = '/viewall/'