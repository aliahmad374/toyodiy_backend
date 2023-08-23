from django.urls import path,include
from cartorder import views


urlpatterns = [    
    path('order/',views.CreateOrderView.as_view(),name='order'),
    path('searchorder/',views.SearchOrderView.as_view(),name='searchorder'),
    path('admin/changeorder/',views.ChangeOrderStatusView.as_view(),name='changeorder'),
]