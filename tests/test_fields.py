# -*- coding: utf-8 -*-
from datetime import date

import solution as f
from solution_dates import ParsedDate


def test_render_date():
    field = ParsedDate(locale='es')
    field.name = u'abc'
    field.load_data(obj_value=date(1979, 5, 13))

    assert field() == field.as_input()
    assert (field(foo='bar') ==
            u'<input foo="bar" name="abc" type="text" value="13/05/1979">')
    assert (field.as_textarea(foo='bar') ==
            u'<textarea foo="bar" name="abc">13/05/1979</textarea>')
    assert (field(foo='bar', type='customdate') ==
            u'<input foo="bar" name="abc" type="customdate" value="13/05/1979">')


def test_render_date_custom():
    field = ParsedDate(locale='es')
    field.name = u'abc'
    field.load_data(obj_value=date(1979, 5, 13))

    assert (field(locale='en_US', format='short') ==
            u'<input name="abc" type="text" value="5/13/79">')
    assert (field(format='long') ==
            u'<input name="abc" type="text" value="13 de mayo de 1979">')
    assert (field(format='d-M-Y') ==
            u'<input name="abc" type="text" value="13-5-1979">')


def test_render_required():
    field = ParsedDate(locale='es', validate=[f.Required])
    field.name = u'abc'
    assert field() == u'<input name="abc" type="text" value="" required>'
    assert field.as_textarea() == u'<textarea name="abc" required></textarea>'


def test_render_default():
    field = ParsedDate(locale='es', default=date(2013, 7, 28))
    field.name = u'abc'
    assert field() == u'<input name="abc" type="text" value="28/07/2013">'


def test_validate_date():
    field = ParsedDate()
    assert field.validate() is None


def test_validate_date_with_default():
    today = date.today()
    field = ParsedDate(default=today)
    assert field.validate() == today


def test_validate_date_with_custom_format():
    field = ParsedDate(validate=[f.Required], locale='es', format='d/M/Y')
    field.load_data(u'15/05/1979')
    assert field.validate() == date(1979, 5, 15)


def test_validate_date_with_named_format():
    field = ParsedDate(validate=[f.Required], locale='es', format='medium')
    field.load_data(u'15/05/1979')
    assert field.validate() == date(1979, 5, 15)

