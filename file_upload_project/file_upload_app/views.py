from django.shortcuts import render

from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello, World from Django!")


def simulate_cdn_upload(request, file_path):
  try:
      # Simulate the upload process
      import uuid
      unique_id = str(uuid.uuid4())
      cdn_url = f'http://cdn.example.com/{unique_id}'
      response_text = f'Uploaded file {file_path} to CDN. CDN URL: {cdn_url}'
      print(response_text)
      return HttpResponse(response_text)
  except Exception as e:
      error_text = f'Error uploading to CDN: {e}'
      print(error_text)
      return HttpResponse(error_text, status=500)