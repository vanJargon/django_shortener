from django import forms
from .models import URLRecord

class RecordURLForm(forms.ModelForm):
	class Meta:
		model = URLRecord
		fields = ['original_url']

