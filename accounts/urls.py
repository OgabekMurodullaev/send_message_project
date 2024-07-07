from django.urls import path
from .views import ContactMessageCreateView, ContactsMessagesView

urlpatterns = [
    path('', ContactMessageCreateView.as_view(), name='xabar_yozish'),
    path('xabarlar/', ContactsMessagesView.as_view(), name='xabarlar'),
]
