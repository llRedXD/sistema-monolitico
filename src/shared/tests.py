from django.test import TestCase
import uuid
from .models import Teste

class ConfirmTest(TestCase):
    def test_validate_UIID(self):  # sourcery skip: avoid-builtin-shadow
        id = str(uuid.uuid4())
        try:
            uuid_obj = uuid.UUID(id, version=4)
        except ValueError:
            return False 
        id_confirm =(str(uuid_obj) == id)
        self.assertIs(id_confirm, True)
        