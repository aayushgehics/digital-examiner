from django.urls import path
from api.views import login_view
urlpatterns=[
path('',login_view)
]