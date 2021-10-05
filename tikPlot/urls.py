from django.urls import path

from . import views

app_name = 'tikPlot'
urlpatterns = [
    path('', views.CountryView.as_view(), name='country'),
    path('<int:regionId>', views.RegionView.as_view(), name='region'),
    path('plot/<int:tikId>', views.TikPlot.as_view(), name='tik'),

]