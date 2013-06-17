# -*- coding: utf-8 -*-
import datetime

import pytest
from solution_dates import parse_date


def test_parser():
    expected = datetime.date(2013, 10, 4)

    assert parse_date(u'04-10-2013', u'd-M-Y') == expected
    assert (parse_date(u'04-10-2013', u'd-M-Y') ==
            parse_date(u'04-10-2013', u'dd-MM-YYYY'))
    assert parse_date(u'10-4-2013', u'M-d-Y') == expected

    assert parse_date(u'4 de octubre de 2013',
                      u"d 'de' MMMM 'de' Y", locale='es') == expected
    assert parse_date(u'4 de octubre de 2013',
                      u"d 'de' MMMM 'de' Y", locale='pt') != expected

    assert parse_date(u'10/4/13', 'short', locale='en') == expected
    assert (parse_date(u'10/4/90', 'short', locale='en') ==
            datetime.date(1990, 10, 4))

    assert parse_date(u'Oct 4, 2013', 'medium', locale='en') == expected

    with pytest.raises(ValueError):
        parse_date(u'04-10-2013', u'dddddddd')

