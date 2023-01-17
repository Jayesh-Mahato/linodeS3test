from django.shortcuts import render


def template(request):
	template="template.html"
	context={}
	return render(request, template, context)