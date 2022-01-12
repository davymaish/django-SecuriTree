from django.urls import path

from . import views

app_name = 'SecuriTree'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('system_hierarchy', views.HierarchyView.as_view(), name='hierarchy'),
    path('manage_doors', views.DoorManageView.as_view(), name='door_manage'),
    path('door_form', views.door_form, name='door_form'),
    path('all_doors', views.DoorsView.as_view(), name='doors'),
    path('manage_doors/door_status', views.door_status, name='door_status'),
]