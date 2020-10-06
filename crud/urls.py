from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name = 'crud/main.html'), name = 'main'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('autos/', views.AutosView.as_view(), name='autos_all'),
    path('autos/main/create', views.AutosCreate.as_view(), name='autos_create'),
    path('autos/main/<int:pk>/update', views.AutosUpdate.as_view(), name='autos_update'),
    path('autos/main/<int:pk>/delete', views.AutosDelete.as_view(), name='autos_delete'),
    path('autos/lookup/', views.MakeView.as_view(), name='make_all'),
    path('autos/lookup/create', views.MakeCreate.as_view(), name='make_create'),
    path('autos/lookup/<int:pk>/update', views.MakeUpdate.as_view(), name='make_update'),
    path('autos/lookup/<int:pk>/delete', views.MakeDelete.as_view(), name='make_delete'),
]