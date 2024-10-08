from django.db import models
from typing    import NewType

import string, random
import datetime
import pytz

from django.conf import settings

PasteId = NewType('PasteId', str)

def mkrandstr(n : int) -> str:
	return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def mkrandstr32() -> str:
	return mkrandstr(32)

def mkpasteid() -> PasteId:
	return PasteId(mkrandstr(24))

# Can't be a lambda: "Cannot serialize function: lambda"
def nowdjangotz():
	return datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))

class Paste(models.Model):
	id      = PasteId(models.SlugField(
		primary_key=True, unique=True, editable=False, blank=True
	))
	content = models.TextField()
	cdate   = models.DateTimeField("creation date",     default=nowdjangotz)
	mdate   = models.DateTimeField("modification date", default=nowdjangotz)
	token   = models.CharField("ownership token",       default=mkrandstr32, max_length=32)

	def save(self, *args, **kwargs):
		while not self.id:
			x = mkpasteid()
			if not Paste.objects.filter(pk=x).exists():
				self.id = x
		super().save(*args, **kwargs)
