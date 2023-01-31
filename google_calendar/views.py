from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#import response from django import response
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect,render
import requests
import os

@api_view(['GET'])
def google_calendar_init(request):
    # Build the authorization URL
    auth_url = f"https://accounts.google.com/o/oauth2/auth?client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.GOOGLE_REDIRECT_URI}&scope={settings.GOOGLE_SCOPE}&response_type=code"
    # Redirect the user to the authorization URL
    return redirect(auth_url)

@api_view(['GET'])
def google_calendar_redirect(request):
    # Get the code from the request
    code = request.GET.get("code")
    print("code",code)
    # Exchange the code for an access token
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    response = requests.post(token_url, data=payload)

    access_token = response.json()["access_token"]

    # Use the access token to get the list of events in the user's calendar
    events_url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    events_response = requests.get(events_url, headers=headers)
    events = events_response.json()["items"]

    return Response(events, status=200)