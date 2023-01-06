from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ClientEngagementForm,ClientDetailForm
from . models import CleintEngament
# Create your views here.

def home(request):
    all_clients=CleintEngament.objects.all()

    return render(request,'home.html',{'all_clients':all_clients})


def entry(request):
    if request.method=='POST':
        form=ClientEngagementForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'client_sheet/successfull.html')
        return render(request,'client_sheet/failure.html')
    form=ClientEngagementForm()
    return render(request,'client_sheet/entryform.html', {'form':form})

    # this the  client detail form

def client_detail(request):
    if request.method=='POST':
        form=ClientDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'client_sheet/successfull.html')
        return render(request,'client_sheet/failure.html')
    form=ClientDetailForm()
    return render(request,'client_sheet/entrydetail.html', {'form':form})

def forms(request):

    return render(request,'forms/forms.html',{})

def engaged_clients(request):
    engaged_clients=CleintEngament.objects.all()
    return render(request,'engaged_clients/engaged_clients.html',{'engaged_clients':engaged_clients})

def client(request,pk):
    client=CleintEngament.objects.filter(pk=pk)
    return render(request,'engaged_clients/client.html',{'client':client})
