from django.shortcuts import render,redirect
from Reader.forms import ReaderForm
from Reader.models import Reader


# Create your views here.
def create_reader(request):
    if request.method =="POST":
        form=ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')


    return render(request, "Reader.html",{'form': ReaderForm})