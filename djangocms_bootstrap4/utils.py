# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_attributes_field import fields

from .constants import TAG_CHOICES


class AttributesField(fields.AttributesField):
    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = _('Attributes')
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        super(AttributesField, self).__init__(*args, **kwargs)


class TagTypeField(models.CharField):
    def __init__(self, *args, **kwargs):
        if 'verbose_name' not in kwargs:
            kwargs['verbose_name'] = _('Tag type')
        if 'choices' not in kwargs:
            kwargs['choices'] = TAG_CHOICES
        if 'default' not in kwargs:
            kwargs['default'] = TAG_CHOICES[0][0]
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'help_text' not in kwargs:
            kwargs['help_text'] = _('Select the HTML tag to be used.')
        super(TagTypeField, self).__init__(*args, **kwargs)
