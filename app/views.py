from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from app.forms import CustomerForm
from app.models import Customers


class CustomersInfo(ListView):
    model = Customers
    template_name = 'component-datatable.html'
    context_object_name = 'customers'
    queryset = Customers.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customers'
        return context






class FormCustomer(FormView):
    model = Customers
    form_class = CustomerForm
    template_name = 'form.html'
    success_url = reverse_lazy('customers')
    context_object_name = 'fields'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'add Customers'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



