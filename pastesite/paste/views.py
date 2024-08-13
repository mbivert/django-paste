from django.shortcuts import render, get_object_or_404
from .models          import Paste
from django.urls      import reverse
from django.http      import HttpResponseRedirect

def paste(request, id):
	p = get_object_or_404(Paste, pk=id)
	c = {"id" : p.id, "content" : p.content }
	return render(request, "paste/paste.html", c)

def index(request):
	return render(request, "paste/index.html")

def new(request):
	p = Paste(content=request.POST["content"])
	p.save()
	return HttpResponseRedirect(reverse("paste:paste", args=(p.id,)))
