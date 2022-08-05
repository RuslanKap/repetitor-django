from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView, ListView

from app.forms import AddressForm
from app.models import Student


class MyForm(FormView):
    template_name = 'form.html'
    form_class = AddressForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def main(request):
    return render(request, 'index.html')


class DashBoard(ListView):
    model = Student
    # A.objects.values("some_a_field", "anoter_a_field", "Bs__some_b_field")
    queryset = Student.objects.values( 'first_name',  'mail', 'second_name', 'telegram_id', 'course__name', 'created_at')
    context_object_name = 'students'
    template_name = 'dashboard.html'
    extra_context = {'title': 'Список учеников'}






