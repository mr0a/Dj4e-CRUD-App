from django.urls import path
from . import views
from django.urls import reverse_lazy

app_name = 'ads'
urlpatterns = [
    path('', views.AdsIndex.as_view(), name='all'),
    path('ads/', views.AdsIndex.as_view()),
    path('ads/<int:pk>/', views.AdsDetail.as_view(), name='article_detail'),
    path('ads/create/', views.AdsCreate.as_view(), name='article_create'),
    path('ads/<int:pk>/update', views.AdsUpdate.as_view(), name='article_update'),
    path('ads/<int:pk>/delete', views.AdsDelete.as_view(), name='article_delete'),
]