from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.views.generic import ListView
from hello_app.models import Service

class CostomerForm(forms.ModelForm):

    license_plate = forms.CharField(max_length=18, required=True,
                          widget = forms.TextInput(attrs={'class': 'form-control'}))

    remark =  forms.CharField(   required=True,
                          widget = forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    class Meta:
        model = Service
        fields = ( 'insure_type', 'customer', 'agent' , 'car_type'    )


def CustomerCreate(request):
    print(request.method)
    if request.method == 'POST':
        form = CostomerForm(request.POST)
        if form.is_valid():
            instances = form.save()
            return redirect(reverse('hello_app:index' ))
    else:
        form = CostomerForm()
    context = {'message': '','form':form}

    return render(request, 'customer.html', context)



class ListCustomerView( ListView):
    model = Service
    paginate_by = 10
    template_name = 'list_customer.html'

    def get_context_data(self, **kwargs):
        context = super(ListCustomerView, self).get_context_data(**kwargs)
        context['page'] = {'menu': 'linenotify_config', 'sub_menu': 'linenotify_config'}
        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self, *args, **kwargs):
        return Service.objects.all().order_by('id')