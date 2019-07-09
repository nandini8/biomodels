from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse,  HttpResponse
from .models import biomodel
from urllib.request import urlopen
import json
from .forms import BioModelForm

# Create your views here.


def add_data():
    obj = biomodel()
    obj.bmKey = "160213582"
    obj.name = "The chemistry of Altzheimers neuropathy acid"
    obj.privacy = 0
    obj.ownerName = "mcgama88"
    obj.save()

    obj.bmKey = "159316751"
    obj.name = "anthocyanin_spot_pattern_old"
    obj.privacy = 0
    obj.ownerName = "mblinov"
    obj.save()

    obj.bmKey = "159058523"
    obj.name = "Ca_Release_Fink_etal_1999\u00262000"
    obj.privacy = 0
    obj.ownerName = "CMC"
    obj.save()

    obj.bmKey = "158495696"
    obj.name = "aMultiVersion"
    obj.privacy = 0
    obj.ownerName = "awillmer"
    obj.save()

    obj.bmKey = "157831511	"
    obj.name = "Macrophage Cargo Capacity"
    obj.privacy = 0
    obj.ownerName = "dantest"
    obj.save()
    # obj = biomodel.objects.all().delete()

def bio_list(request):
    bio_objects = biomodel.objects.all()
    data = {"results": list(bio_objects.values())}
    add_data()
    return JsonResponse(data)


def bio_detail(request, key):
    bio_objects = get_object_or_404(biomodel, bmKey=key)
    print(bio_objects.column)
    data = {"results": {
        'bmKey': bio_objects.bmKey,
        'name': bio_objects.name,
    }}
    return JsonResponse(data)

def access_data(request):
    if request.method == 'POST':
        bmName = request.POST.get('bmName').replace(" ","+")
        bmId = request.POST.get('bmId')
        category = request.POST.get('category')
        owner = request.POST.get('owner')
        savedLow = request.POST.get('savedLow')
        savedHigh = request.POST.get('savedHigh')
        sartRow = request.POST.get('startRow')
        maxRows = request.POST.get('maxRows')
        orderBy = request.POST.get('orderBy')
        # print(bmKey)
        url = '/search?bmName='+bmName+'&bmId='+str(bmId)+'&category='+category+'&owner='+owner+'&savedLow='+savedLow+'&savedHigh='+savedHigh+'&startRow='+str(sartRow)+'&maxRows='+str(maxRows)+'&orderBy='+orderBy
        print(url)
        # data = urlopen(url).read()
        # data = json.loads(data)
        # print("Data", data)
        return redirect(url)
    else:
        return render(request, 'index.html')

def biomodel_new(request):
    if request.method == "POST":
        form = BioModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.bmKey = request.POST.get('bmKey')
            post.name = request.POST.get('name')
            post.prvacy = request.POST.get('privacy')
            post.save()
        return redirect('/biomodels')
    else:
        form = BioModelForm()
        return render(request, 'addrecord.html', {'form': form})

def publication(request):
    return HttpResponse("<h1>Publication</h1>")
def simstatus(request):
    return HttpResponse("<h1>Simulation Status</h1>")
def simtask(request):
    return HttpResponse("<h1>Simulation Task</h1>")
def application(request, key):
    return HttpResponse("<h1>Simulation for "+ key +"</h1>")
def loginform(request):
    return render(request, 'signin.html')
def login(request):
    return HttpResponse("<h1>Login</h1>")
