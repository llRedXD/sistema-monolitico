from django.db import models
import uuid

class TesteUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class TesteEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    rel_users = models.ManyToManyField("TesteUser", related_name='TesteEmpresa')

    def __str__(self):
        return self.name

class TesteProgramador(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

