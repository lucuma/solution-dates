# -*- coding: utf-8 -*-
from babel.dates import format_date  # , format_datetime, format_time
from solution import Text, Markup, IsDate, get_html_attrs

from ..parser import parse_date


class ParsedDate(Text):

    """A date field with custom format

    :param format:
        When returned as a string, the value will be printed using this format.

    :param validate:
        An list of validators. This will evaluate the current `value` when
        the method `validate` is called.

    :param default:
        Default value. It must be a `date` or `datetime`.

    :param prepare:
        An optional function that takes the current value as a string
        and preprocess it before rendering.

    :param clean:
        An optional function that takes the value already converted to
        python and return a 'cleaned' version of it. If the value can't be
        cleaned `None` must be returned instead.

    :param hide_value:
        Do not render the current value a a string. Useful with passwords
        fields.

    :param locale:
        Default locale for this field. Overwrite the form locale.

    :param tz:
        Default timezone for this field. Overwrite the form timezone.

    """
    _type = 'text'  # HTML5's type="date" can only read yyy-MM-dd format
    default_validator = IsDate
    format = 'medium'
    locale = 'en'

    def __init__(self, format=None, locale=None, **kwargs):
        self.format = format or self.format
        self.locale = locale.replace('-', '_') if locale else self.locale
        kwargs.setdefault('default', None)
        return super(ParsedDate, self).__init__(**kwargs)

    def py_to_str(self, format=None, locale=None, **kwargs):
        dt = self.obj_value or self.default
        if not dt:
            return u''
        format = format or self.format
        locale = locale.replace('-', '_') if locale else self.locale
        return format_date(dt, format=format, locale=locale)

    def as_input(self, format=None, locale=None, **kwargs):
        kwargs['type'] = kwargs.setdefault('type', self._type)
        kwargs['name'] = self.name
        kwargs['value'] = self.to_string(
            format=format, locale=locale, **kwargs)
        if not self.optional:
            kwargs.setdefault('required', True)
        html = u'<input %s>' % get_html_attrs(kwargs)
        return Markup(html)

    def as_textarea(self, format=None, locale=None, **kwargs):
        kwargs['name'] = self.name
        if not self.optional:
            kwargs.setdefault('required', True)
        html_attrs = get_html_attrs(kwargs)
        value = self.to_string(format=format, locale=locale, **kwargs)
        html = u'<textarea %s>%s</textarea>' % (html_attrs, value)
        return Markup(html)

    def str_to_py(self, format=None, locale=None):
        if not self.str_value:
            return self.default or None
        format = format or self.format
        locale = locale.replace('-', '_') if locale else self.locale
        return parse_date(self.str_value, format, locale)

