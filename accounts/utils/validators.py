import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

cell_phone_validator = RegexValidator(
    regex=r'^(09|9)\d{9}$',
    message='Start with 09/9 and it must 9 digits after that. For example: 09120000000 or 9120000000')


def validate_national_code(code):
    if not re.search('^[0-9]{10}$', code):
        raise ValidationError(
            _('%(value)s is not an correct national_id'),
            params={'value': code},
        )
    for i in range(10):
        if re.search('^'+str(i)+'{10}$', code):
            raise ValidationError(
                _('%(value)s is not an correct national_id'),
                params={'value': code},
            )
    sum = 0
    for i in range(9):
        sum += ((10-i)*int(code[i:i+1]))
    ret = sum % 11
    parity = int(code[9:10])
    if ((ret < 2 and ret == parity) or (ret >= 2 and ret == 11-parity)):
        return True
    raise ValidationError(
        _('%(value)s is not an correct national_id'),
        params={'value': code},
    )
