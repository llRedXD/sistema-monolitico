# sourcery skip: avoid-builtin-shadow
from django.db import models
import uuid

class Teste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) 

    def __str__(self):
        return self.name
