from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:thread>/', views.thread_view, name='thread'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:thread>/', views.getMessages, name='getMessages'),
    path('delete_thread/<str:thread>/', views.delete_thread, name='delete_thread'),
    path('get_unread_messages_count/<str:thread>/', views.get_unread_messages_count, name='get_unread_messages_count'),
]
