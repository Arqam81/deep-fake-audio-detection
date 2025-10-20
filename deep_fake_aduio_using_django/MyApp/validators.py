from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>1048576000:
        raise ValidationError("maximum  size is 10 mb")