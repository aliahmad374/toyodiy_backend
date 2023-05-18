from django.urls import path
from after_login import views


urlpatterns = [    
    path('user_vehicle/',views.UserVehicleView.as_view(),name='vehicle'),
]