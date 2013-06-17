# -*- coding: utf-8 -*-
import datetime
import re
import sys

from babel import Locale
from babel.dates import parse_pattern


PY2 = sys.version_info[0] == 2


def iteritems(d, **kw):
    """Return an iterator over the (key, value) pairs of a dictionary."""
    if not PY2:
        return iter(d.items(**kw))
    return d.iteritems(**kw)


def itervalues(d, **kw):
    """Return an iterator over the values of a dictionary."""
    if not PY2:
        return iter(d.values(**kw))
    return d.itervalues(**kw)


def parse_date(value, pattern, locale='en'):
    loc = Locale(locale)
    regex = get_regex_from_pattern(pattern, loc)
    match = re.match(regex, value, re.IGNORECASE)
    if not match:
        return None
    year = extract_year(match.group('year'))
    month = extract_month(match.group('month'), loc)
    day = int(match.group('day'))
    try:
        return datetime.date(year, month, day)
    except ValueError:
        return None


def get_regex_from_pattern(pattern, loc):
    if pattern in loc.date_formats:
        format = loc.date_formats[pattern].format
    elif pattern in loc.datetime_formats:
        format = loc.datetime_formats[pattern].format
    else:
        format = parse_pattern(pattern).format
    return format % get_locale_date_dict(loc)


def get_locale_date_dict(loc):
    ld = {
        'y': r'(?P<year>[0-9]{4})',
        'Y': r'(?P<year>[0-9]{4})',
        'yy': r'(?P<year>[0-9]{2})',
        'YY': r'(?P<year>[0-9]{2})',
        'yyy': r'(?P<year>[0-9]{4})',
        'YYY': r'(?P<year>[0-9]{4})',
        'yyyy': r'(?P<year>[0-9]{4})',
        'YYYY': r'(?P<year>[0-9]{4})',
        'M': r'(?P<month>[0-9]{1,2})',
        'L': r'(?P<month>[0-9]{1,2})',
        'MM': r'(?P<month>[0-9]{1,2})',
        'LL': r'(?P<month>[0-9]{1,2})',
        'MMM': get_months(loc, 'abbreviated'),
        'MMMM': get_months(loc, 'wide'),
        'MMMMM': get_months(loc, 'narrow'),
        'd': r'(?P<day>[0-9]{1,2})',
        'dd': r'(?P<day>[0-3][0-9])',
    }
    ld['LLL'] = ld['MMM']
    ld['LLLL'] = ld['MMMM']
    ld['LLLLL'] = ld['MMMMM']
    return ld


def get_months(loc, key):
    values = itervalues(loc.months['format'][key])
    items = get_escaped_pattern(values)
    return r'(?P<month>' + r'|'.join(items) + r')'


def get_days(loc, key):
    values = itervalues(loc.days['format'][key])
    items = get_escaped_pattern(values)
    return r'|'.join(items),


def get_escaped_pattern(items):
    return [re.escape(v).replace(r'\.', r'\.?') for v in items]


def extract_year(value):
    year = int(value)
    if len(str(year)) > 2:
        return year
    curr_year = datetime.date.today().year
    year = get_century(curr_year) + year
    if year < curr_year + 50:
        return year
    return year - 100


def get_century(curr_year):
    return int(str(curr_year)[:2] + '00')


def extract_month(value, loc):
    if value.isdigit():
        return int(value)
    months = loc.months['format']
    for grkey, mdict in iteritems(months):
        for k, v in iteritems(mdict):
            if v == value:
                return k

