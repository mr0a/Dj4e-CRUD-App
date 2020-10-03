from django.urls import path
from . import views

urlpatterns = [
    path('', views.CatsView.as_view(), name='cats_list'),
    path('lookup/', views.BreedsView.as_view(), name='breeds_list'),
    path('lookup/create/', views.BreedsCreate.as_view(), name='breeds_create'),
    path('lookup/create/<int:pk>/update', views.BreedsUpdate.as_view(), name='breeds_update'),
    path('lookup/create/<int:pk>/delete', views.BreedsDelete.as_view(), name='breeds_delete'),
    path('main/create/', views.CatsCreate.as_view(), name='cats_create'),
    path('main/create/<int:pk>/update', views.CatsUpdate.as_view(), name='cats_update'),
    path('main/create/<int:pk>/delete', views.CatsDelete.as_view(), name='cats_delete'),
]