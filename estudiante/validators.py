from django.core.exceptions import ValidationError
import re

def validar_mayor_5(value):
   if len(value) <= 5:
      raise ValidationError("%(value)s es demasiado corto", params={'value': value})
   
def validar_solo_letras(value):
   if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ ]*$", value):
      raise ValidationError('El nombre solo debe contener letras.')