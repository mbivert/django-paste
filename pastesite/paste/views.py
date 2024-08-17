from django.shortcuts import render, get_object_or_404
from .models          import Paste
from django.urls      import reverse
from django.http      import HttpResponseRedirect
from django.utils     import timezone

def paste(request, id):
	p = get_object_or_404(Paste, pk=id)
	try:
		token = request.session['token_%s' % p.id]
	except KeyError:
		token = ""

	try:
		error = request.session.pop("error")
	except KeyError:
		error = ""

	c = {
		"id"      : p.id,
		"cdate"   : p.cdate,
		"mdate"   : p.mdate,
		"content" : p.content,
		"token"   : token,
		"error"   : error,
	}
	return render(request, "paste/paste.html", c)

def index(request):
	return render(request, "paste/index.html")

def new(request):
	p = Paste(content=request.POST["content"])
	p.save()
	request.session['token_%s' % p.id] = p.token
	return HttpResponseRedirect(reverse("paste:paste", args=(p.id,)))

def do(request):
	id      = request.POST["id"]
	token   = request.POST["token"]
	action  = request.POST["action"]
	content = request.POST["content"]

	print(id, content)

	p  = get_object_or_404(Paste, pk=id)
	if token != p.token:
		request.session["error"] = "Failed to validate ownership!"
	elif action == "edit":
		p.content = content
		p.mdate   = timezone.now()
		p.save()
	elif action == "delete":
		p.delete()
		return HttpResponseRedirect(reverse("paste:index"))
	else:
		request.session["error"] = "( ͡° ͜ʖ ͡°)"

	return HttpResponseRedirect(reverse("paste:paste", args=(p.id,)))
