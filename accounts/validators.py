import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
