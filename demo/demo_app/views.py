from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import biomodel
from urllib.request import urlopen
import json
from .forms import BioModelForm

# Create your views here.

def bio_list(request):
    bio_objects = biomodel.objects.all()
    data = {"results": list(bio_objects.values('bmKey', 'name'))}
    return JsonResponse(data)


def bio_detail(request, key):
    bio_objects = get_object_or_404(biomodel, bmKey=key)[0]
    data = {"results": {
        'bmKey': bio_objects.bmKey,
        'name': bio_objects.name,
    }}
    return JsonResponse(data)

def access_data(request):
    if request.method == 'POST':
        
        data = urlopen('http://127.0.0.1:8000/biomodels').read()
        data = json.loads(data)
        return  render(request, 'index.html', {'data': data})
    else:
        return render(request, 'index.html')

def biomodel_new(request):
    if request.method == "POST":
        form = BioModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.bmKey = request.bmKey
            post.name = request.name
            post.prvacy = request.privacy
            post.save()
            return redirect('biomodels')
    else:
        form = BioModelForm()
        return render(request, 'addrecord.html', {'form': form})