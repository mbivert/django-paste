from django.shortcuts import render, get_object_or_404
from .models          import Paste

def paste(request, id):
	p = get_object_or_404(Paste, pk=id)
	c = {"id" : p.id, "content" : p.content }
	return render(request, "paste/paste.html", c)
