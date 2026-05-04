from django.http import JsonResponse
import time

def test_api(request):
    time.sleep(0.1)
    return JsonResponse({"message": "Hello from Django"})