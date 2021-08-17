from stdnum import isbn

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def isbn_validator(isbn_number: str) -> bool:
    if not isbn.is_valid(isbn_number):
        raise ValidationError(_("Invalid ISBN number"))
    return True