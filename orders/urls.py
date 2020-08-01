from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("menu", views.menu, name="menu"),
    path("verzeo", views.verzeo, name="verzeo"),
    path("customize/<str:cat>/<str:itemname>/",  views.customize, name="customize"),
    path("add/<str:cat>/<str:itemname>/", views.add, name="add"),
    path('cart', views.cart, name='cart'),
    path('place', views.place, name='place'),
    path('orders', views.ordershow, name='ordershow'),
    path('adminview', views.adminview, name='adminview'),
    path('complete/<int:oid>', views.complete, name='complete')
]
