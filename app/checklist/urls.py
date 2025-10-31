from django.urls import path
from app.checklist.views import checklist
from django.urls import path


urlpatterns = [
    path('', checklist, name='checklist-form')
]
