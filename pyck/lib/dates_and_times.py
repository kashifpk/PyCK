"""
Classes for working with Dates and Times and translating them to python's native Date, Time and DateTime objects

Basically these serve as a wrapper around code to get parts of dates and times so that further processing
can be performed on those objects
"""

from datetime import date, time, datetime
from dateutil.relativedelta import relativedelta


class Date(object):
    year = None
    month = None
    day = None

    def __init__(self, year=None, month=None, day=None):
        if year: self.year = int(year)
        if month: self.month = int(month)
        if day: self.day = int(day)

    @classmethod
    def from_string(cls, date_str):
        "Populate date components from date string of the format YYYY[-MM[-DD]]"
        
        parts = date_str.split('-')
        obj = cls()

        if len(parts)>0: obj.year = int(parts[0])
        if len(parts)>1: obj.month = int(parts[1])
        if len(parts)>2: obj.day = int(parts[2])

        return obj

    def is_empty(self):
        "Returns True if all fields are None"

        if self.year or self.month or self.day:
            return False

        return True

    def is_partial(self):
        "Returns True if there is any date field missing, else returns False"

        if self.year and self.month and self.day:
            return False

        return True

    def to_native(self):
        "Converts to native date type and returns the object. Works only if the date is not partial"

        assert False == self.is_partial()

        return date(year=self.year, month=self.month, day=self.day)

    def range(self):
        """
        return two dates covering the whole range for a partial date.
        For a complete date, the same date is returned twice
        Returned dates are converted to native date type.
        """

        if not self.is_partial():
            return (self.to_native(), self.to_native())
        else:
            if not self.month:  # cover whole year if no month given
                return (date(self.year, 1, 1), date(self.year, 12, 31))

            elif not self.day:  # cover whole month if no day given
                d = (date(self.year, self.month, 1) + relativedelta(months=1)) - relativedelta(days=1)
                return (date(self.year, self.month, 1), d)


class Time(object):
    hour = None
    minute = None
    second = None
    microsecond = None

    def __init__(self, hour=None, minute=None, second=None, microsecond=None):
        if hour: self.hour = int(hour)
        if minute: self.minute = int(minute)
        if second: self.second = int(second)
        if microsecond: self.microsecond = int(microsecond)

    @classmethod
    def from_string(cls, time_str):
        "Populate time components from time string of the format HH[:MM[:SS[.microseconds]]]"
        
        parts = time_str.split(':')
        obj = cls()

        if len(parts)>0: obj.hour = int(parts[0])
        if len(parts)>1: obj.minute = int(parts[1])
        
        if len(parts)>2:
            if '.' in parts[2]:
                second_parts = parts[2].split('.')
                obj.second = int(second_parts[0])
                obj.microsecond = int(second_parts[1])
            else:
                obj.second = int(parts[2])

        return obj

    def is_empty(self):
        "Returns True if all fields are None"

        if self.hour or self.minute or self.second or self.microsecond:
            return False

        return True

    def is_partial(self):
        "Returns True if there is any time field missing, else returns False"

        if self.hour and self.minute and self.second and self.microsecond:
            return False

        return True

    def to_native(self):
        "Converts to native time type and returns the object. Works only if the time is not partial"

        assert False == self.is_partial()

        return time(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond)

    def range(self):
        """
        return two times covering the whole range for a partial time.
        For a complete time, the same time is returned twice
        Returned times are converted to native time type.
        """

        if not self.is_partial():
            return (self.to_native(), self.to_native())
        else:
            if not self.minute:  # cover whole hour if no minute given
                return (time(self.hour, 0, 0), time(self.hour, 59, 59, 999999))

            elif not self.second:  # cover whole minute if no second given
                return (time(self.hour, self.minute, 0), time(self.hour, self.minute, 59, 999999))
            
            elif not self.microsecond:  # cover whole second if no microsecond given
                return (time(self.hour, self.minute, self.second), time(self.hour, self.minute, self.second, 999999))


class DateTime(Date, Time):

    def __init__(self, year=None, month=None, day=None,
                 hour=None, minute=None, second=None, microsecond=None):

        Date.__init__(self, year, month, day)
        Time.__init__(self, hour, minute, second, microsecond)

    @classmethod
    def from_string(cls, datetime_str):
        "Populate the DateTime object using string of format YYYY[-MM[-DD]][ HH[:MM[:SS[.microseconds]]]]"

        obj = cls()
        parts = datetime_str.split(' ')
        date_obj = Date.from_string(parts[0])
        time_obj = Time()
        if len(parts)>1:
            time_obj = Time.from_string(parts[1])

        obj.day = date_obj.day
        obj.month = date_obj.month
        obj.year = date_obj.year
        obj.hour = time_obj.hour
        obj.minute = time_obj.minute
        obj.second = time_obj.second
        obj.microsecond = time_obj.microsecond

        return obj

    def is_empty(self):
        "Returns True if all fields are None"

        return Date.is_empty(self) and Time.is_empty(self)

    def is_partial(self):
        "Returns True if there is any date or time field missing, else returns False"

        return Date.is_partial(self) or Time.is_partial(self)

    def to_native(self):
        "Converts to native datetime type and returns the object. Works only if the DateTime is not partial"

        assert False == self.is_partial()

        return datetime(year=self.year, month=self.month, day=self.day,
                        hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond)

    def range(self):
        """
        return two datetimes covering the whole range for a partial datetime.
        For a complete datetime, the same datetime is returned twice
        Returned datetimes are converted to native datetime type.
        """

        if not self.is_partial():
            return (self.to_native(), self.to_native())
        else:
            if not self.month:  # cover whole year if no month given
                return (datetime(year=self.year, month=1, day=1),
                        datetime(year=self.year, month=12, day=31,
                                 hour=23, minute=59, second=59, microsecond=999999))

            elif not self.day:  # cover whole month if no day given
                d = (datetime(self.year, self.month, 1) + relativedelta(months=1)) - relativedelta(days=1)
                d = d.replace(hour=23, minute=59, second=59, microsecond=999999)
                return (datetime(self.year, self.month, 1), d)

            elif not self.hour:  # cover the whole day if no hour given
                return (datetime(year=self.year, month=self.month, day=self.day),
                        datetime(year=self.year, month=self.month, day=self.day,
                                 hour=23, minute=59, second=59, microsecond=999999))

            if not self.minute:  # cover whole hour if no minute given
                return (datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour),
                        datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour, minute=59, second=59, microsecond=999999))

            elif not self.second:  # cover whole minute if no second given
                return (datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour, minute=self.minute),
                        datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour, minute=self.minute, second=59, microsecond=999999))
            
            elif not self.microsecond:  # cover whole second if no microsecond given
                return (datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour, minute=self.minute, second=self.second),
                        datetime(year=self.year, month=self.month, day=self.day,
                                 hour=self.hour, minute=self.minute, second=self.second, microsecond=999999))
