from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from django.views import generic
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Door, Area, AccessRule, User


class IndexView(TemplateView):
    template_name = 'SecuriTree/index.html'

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'SecuriTree/home.html'

class HierarchyView(LoginRequiredMixin,generic.ListView):
    model = Area
    template_name = 'SecuriTree/hierarchy.html'

    context_object_name = 'area_list'

    def get_queryset(self):
        return Area.objects.filter(parent_area__isnull=True).order_by('id')

class DoorManageView(LoginRequiredMixin,TemplateView):
    template_name = 'SecuriTree/manage_doors.html'

class DoorsView(LoginRequiredMixin,generic.ListView):
    model = Door
    template_name = 'SecuriTree/all_doors.html'

    context_object_name = 'door_list'

    def get_queryset(self):
        return Door.objects.all()

@login_required
def door_form(request):
    r_action = request.GET['action']

    if r_action == 'unlock':
        action = 'unlock'
    else:
        action = 'lock'
    
    return render(request, 'SecuriTree/door_form.html', {'action':action})

@login_required
def door_status(request):

    door_id = request.POST['doorid']
    status = request.POST['status']

    door = get_object_or_404(Door, pk=door_id)
    # door = Door.objects.filter(pk = door_id).first()

    door.status = status;
    door.save()

    if status == 'closed':
        msg = 'Door ' + door.id + ' successfully locked.'
    else:
        msg = 'Door ' + door.id + ' successfully unlocked.'
    
    messages.success(request, msg)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
