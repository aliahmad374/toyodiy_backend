from django.urls import path
from search_api import views

urlpatterns = [
    path('manufacture/', views.ManufactureAPI.as_view()),
    path('model/', views.ModelAPI.as_view()),
    path('type/', views.Type_YearAPI.as_view()),
    path('vehicle/', views.VehicleAPI.as_view()),
    path('category/', views.CategoryAPI.as_view()),
    path('subcategory/', views.SubCategoryAPI.as_view()),
    path('part/', views.PartsAPI.as_view()),
    path('part_detail/', views.PartsDetailAPI.as_view()),
    path('part_number/', views.PartsNumberAPI.as_view()),
    path('autocomplete/', views.AutoComplete.as_view()),
]



