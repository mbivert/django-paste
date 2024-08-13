from django.db import models
from typing    import NewType

import string, random

PasteId = NewType('PasteId', str)

def mkpasteid() -> PasteId:
	return PasteId(''.join(random.choices(string.ascii_letters + string.digits, k=24)))

class Paste(models.Model):
	id      = PasteId(models.SlugField(
		primary_key=True, unique=True, editable=False, blank=True
	))
	content = models.TextField()

	def save(self, *args, **kwargs):
		while not self.id:
			x = mkpasteid()
			if not Paste.objects.filter(pk=x).exists():
				self.id = x
		super().save(*args, **kwargs)
