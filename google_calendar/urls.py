from django.urls import path
from .views import google_calendar_init, google_calendar_redirect

urlpatterns = [
    path('rest/v1/calendar/init/', google_calendar_init, name='google_calendar_init'),
    path('rest/v1/calendar/redirect/', google_calendar_redirect, name='google_calendar_redirect'),
    path('accounts/google/login/callback/', google_calendar_redirect, name='google_calendar_redirect'),
    
]