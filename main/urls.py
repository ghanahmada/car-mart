from django.urls import path
from main.views import show_author, show_content

app_name = 'main'

urlpatterns = [
    path('', show_author, name='show_author'),
]