from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os

class Biologists(APIView):
    def get(self, request):
        SUPABASE_URL = os.environ.get("SUPABASE_REST_API_BIOLOGISTS_URL")
        SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"{SUPABASE_URL}?order=birthyear.asc", headers=headers)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"error": "Unable to fetch data"}, status=response.status_code)


class ComputerScientists(APIView):
    def get(self, request):
        SUPABASE_URL = os.environ.get("SUPABASE_REST_API_COMPUTERSCIENTISTS_URL")
        SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.get(f"{SUPABASE_URL}?order=birthyear.asc", headers=headers)

        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"error": "Unable to fetch data"}, status=response.status_code)