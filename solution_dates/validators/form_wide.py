# -*- coding: utf-8 -*-
import datetime

from solution import FormValidator


class ValidSplitDate(FormValidator):
    """Form validator that assert that a date splitted in two or three separate
    fields is valid.

    :param day:
        Name of the day field.

    :param month:
        Name of the month field.

    :param year:
        Name of the year field (optional, assumed the current one).

    :param message:
        Custom error message.
    
    """
    message = u'This is not a valid date.'
    
    def __init__(self, day, month, year=None, message=None):
        self.day = day
        self.month = month
        self.year = year
        if message is not None:
            self.message = message

    def __call__(self, data=None, form=None):
        now = datetime.date.today()
        try:
            day = int(data.get(self.day))
            month = int(data.get(self.month))
            year = int(data.get(self.year)) if self.year else None
            if year:
                d = datetime.date(year, month, day)
            else:
                d = datetime.date(now.year, month, day)
        except Exception:
            return False
        return True

