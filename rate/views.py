from django.shortcuts import render
from models import Rate
from forms import RateForm

def index(request):
	rates = Rate.objects.all()
	return render(request,'rate/rates.html',{'rates':rates})

def add_rate(request):
	if request.method == "POST":
		form = RateForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			rates = Rate.objects.all()
			return render(request,'rate/rates.html',{'rates':rates,'success_added':1})
	form = RateForm()
	return render(request,'rate/add_rate.html',{'form':form,'added':1})


def edit_rate(request,rate_id):
	rate = Rate.objects.all().filter(pk=rate_id)[0]
	if request.method == "POST":
		form = RateForm(request.POST,instance=rate)
		if form.is_valid():
			rates = Rate.objects.all()
			form.save(commit=True)
			return render(request,'rate/rates.html',{'rates':rates,'success_edited':1})
	else:
		form = RateForm(instance=rate)
		return render(request,'rate/add_rate.html',{'form':form,'edited':1,'rate_id':rate_id})
