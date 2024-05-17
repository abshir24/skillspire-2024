from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index),
    path('login', views.login),
    path('register', views.register),
    path('newsfeed', views.newsfeed),
    path('addpost', views.addpost),
    path('edit/<int:id>',views.editpost),
    path('delete/<int:id>',views.deletepost)
    # path('showid/<int:id>',views.showid),
    # path('handleformdata',views.formdata),
    # path('sessiondata',views.sessiondata),
]