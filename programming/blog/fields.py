import re
from django.db import models
from django.forms import ValidationError
from .validators import phone_number_validator,zip_code_check
from .validators import zip_code_validator, ZipCodeValidator

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators',[])
        kwargs['validators'].append(phone_number_validator)
        super().__init__(*args, **kwargs)


class ZipCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', 0)
        kwargs.setdefault('max_length', 5)
        kwargs.setdefault('validators',[])
        kwargs['validators'].append(zip_code_validator)
        kwargs['validators'].append(zip_code_check)
        super().__init__(*args, **kwargs)

class ZipCodeField_ver_2(models.CharField):
    default_validators = [ZipCodeField(True)]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('default', 0)
        kwargs.setdefault('max_length', 20)
        super().__init__(*args, **kwargs)