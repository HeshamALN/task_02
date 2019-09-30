from django.shortcuts import render
# from django.http import HttpRespponse


# Create your views here.


def restaurants(request):
	context ={
	"msg":"Hello World!"
	}
	
	return render(request, 'html.html', context)
