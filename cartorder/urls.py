from django.urls import path,include
from cartorder import views


urlpatterns = [    
    path('order/',views.CreateOrderView.as_view(),name='order'),
    path('order_notlogin/',views.CreateNotLoginOrderView.as_view(),name='notloginorder'),
    path('vieworder/',views.SearchOrderView.as_view(),name='vieworder'),
    path('admin/changeorder/',views.ChangeOrderStatusView.as_view(),name='changeorder'),
    path('myorders/',views.MyOrdersView.as_view(),name='myorders'),
    path('get_order_by_car/',views.get_orders_by_car_linkage_id,name='myordersbycar'),
    path('payment_response/',views.payment_response,name='paymentresponse'),
    path('payment_callback/',views.payment_callback_response,name='paymentcallback'),

]