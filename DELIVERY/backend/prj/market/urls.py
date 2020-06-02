from django.urls import path, include
from market.views.auth import AuthView, hello
from market.views.product import ProductlistView

urlpatterns = [ 
        path('userlogin',AuthView.as_view()),
        path('hello',hello),
        path('product_list',ProductlistView.as_view())
]
