from django.urls import path
#from django.urls.resolvers import URLPattern    
from order import views

urlpatterns=[
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),

]