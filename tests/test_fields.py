# -*- coding: utf-8 -*-
from datetime import date, datetime

import pytest
import solution as f
from solution_dates import Date


def test_render_date():
    field = Date(locale='es')
    field.name = u'abc'
    field.load_data(obj_value=date(1979, 5, 13))

    assert unicode(field) == field() == field.as_input()
    assert (field(foo='bar') ==
            u'<input foo="bar" name="abc" type="date" value="13/05/1979">')
    assert (field.as_textarea(foo='bar') ==
            u'<textarea foo="bar" name="abc">13/05/1979</textarea>')
    assert (field(foo='bar', type='text') ==
            u'<input foo="bar" name="abc" type="text" value="13/05/1979">')


def test_render_date_custom():
    field = Date(locale='es')
    field.name = u'abc'
    field.load_data(obj_value=date(1979, 5, 13))

    assert (field(locale='en_US', format='short') ==
            u'<input name="abc" type="date" value="5/13/79">')
    assert (field(format='long') ==
            u'<input name="abc" type="date" value="13 de mayo de 1979">')
    assert (field(format='d-M-Y') ==
            u'<input name="abc" type="date" value="13-5-1979">')


def test_render_required():
    field = Date(locale='es', validate=[f.Required])
    field.name = u'abc'
    assert field() == u'<input name="abc" type="date" value="" required>'
    assert field.as_textarea() == u'<textarea name="abc" required></textarea>'


def test_render_default():
    field = Date(locale='es', default=date(2013, 7, 28))
    field.name = u'abc'
    assert field() == u'<input name="abc" type="date" value="28/07/2013">'


def test_validate_date_with_custom_format():
    field = Date(validate=[f.Required], locale='es', format='d/M/Y')
    field.load_data(u'15/05/1979')
    assert field.validate() == date(1979, 5, 15)


def test_validate_date_with_named_format():
    field = Date(validate=[f.Required], locale='es', format='medium')
    field.load_data(u'15/05/1979')
    assert field.validate() == date(1979, 5, 15)

