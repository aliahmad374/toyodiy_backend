from django.urls import path,include
from cartorder import views


urlpatterns = [    
    path('order/',views.CreateOrderView.as_view(),name='order'),
    path('vieworder/',views.SearchOrderView.as_view(),name='vieworder'),
    path('admin/changeorder/',views.ChangeOrderStatusView.as_view(),name='changeorder'),
    path('myorders/',views.MyOrdersView.as_view(),name='myorders'),
]