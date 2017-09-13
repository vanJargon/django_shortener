from django.shortcuts import render, get_object_or_404, redirect
from .models import URLRecord

# Create your views here.
def index(request):
	return render(request, 'shortener_app/index.html', {})

def redirect_url(request, pk):
	url = get_object_or_404(URLRecord, pk=pk).original_url
	return redirect(url)
