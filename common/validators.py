from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_mb, message=None):
        self.max_mb = max_mb
        # Convert MB to Bytes (1 MB = 1024 * 1024 bytes)
        self.max_bytes = max_mb * 1024 * 1024
        self.message = message or f"Maximum file size allowed is {max_mb}MB."

    def __call__(self, value):
        if value.size > self.max_bytes:
            raise ValidationError(self.message)

    def __eq__(self, other):
        return (
            isinstance(other, FileSizeValidator) and
            self.max_mb == other.max_mb and
            self.message == other.message
        )



@deconstructible
class RangeValidator:
    def __init__(self, min_value, max_value, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message or f"Value must be between {min_value} and {max_value}."

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValidationError(self.message)

    def __eq__(self, other):
        return (
                isinstance(other, RangeValidator) and
                self.min_value == other.min_value and
                self.max_value == other.max_value and
                self.message == other.message
        )
