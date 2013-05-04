# -*- coding: utf-8 -*-
import pytest
from solution_dates import Date


# def test_render_text():
#     field = f.Text()
#     field.name = u'abc'
#     field.load_data(u'123')

#     assert unicode(field) == field() == field.as_input()
#     assert (field(foo='bar') ==
#             u'<input foo="bar" name="abc" type="text" value="123">')
#     assert (field.as_textarea(foo='bar') ==
#             u'<textarea foo="bar" name="abc">123</textarea>')
#     assert (field(foo='bar', type='email') ==
#             u'<input foo="bar" name="abc" type="email" value="123">')

#     field = f.Text(hide_value=True)
#     field.name = u'abc'
#     field.load_data(u'123')
#     assert (field(foo='bar', type='password') ==
#             u'<input foo="bar" name="abc" type="password" value="">')


# def test_validate_text():
#     field = f.Text(validate=[f.Required])
#     field.name = u'abc'
#     field.load_data(u'123')
#     assert field.validate() == u'123'

#     field = f.Text(hide_value=True, validate=[f.Required])
#     field.name = u'abc'
#     field.load_data(u'123')
#     assert field.validate() == u'123'

