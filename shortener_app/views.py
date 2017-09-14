from django.shortcuts import render, get_object_or_404, redirect
from .models import URLRecord
from .shortening_algo import saturate, dehydrate
from .forms import RecordURLForm

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = RecordURLForm(request.POST)
		if form.is_valid():
			url_record = form.save(commit=False)
			url_record.save()
	else:
		form = RecordURLForm()
	return render(request, 'shortener_app/index.html', {'form':form})

def redirect_url(request, base):
	pk = saturate(base)
	url = get_object_or_404(URLRecord, pk=pk).original_url
	return redirect(url)
