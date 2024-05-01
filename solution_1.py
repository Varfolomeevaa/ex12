class Date:
    """
    Represents a date and provides methods for date manipulation and comparison.

    Attributes:
        days (dict): A dictionary containing the number of days for each month.
        month (dict): A dictionary mapping month numbers to their abbreviated names.

    Methods:
        __init__: Initializes a Date object with a given date string.
        leap_year: Static method to determine if a given year is a leap year.
        check_date: Instance method to validate the format and correctness of the date string.
        date: Getter property to retrieve the formatted date string.
        date.setter: Setter property to set the date from a given string.
        to_timestamp: Instance method to count time since 1970.
        __eq__: Instance method to check equality between two Date objects.
        __ne__: Instance method to check inequality between two Date objects.
        __lt__: Instance method to check if one Date object is less than another.
        __le__: Instance method to check if one Date object is less than or equal to another.
        __gt__: Instance method to check if one Date object is greater than another.
        __ge__: Instance method to check if one Date object is greater than or equal to another.
        __str__: Instance method to return a string representation of the Date object.
        __repr__: Instance method to return a string representation of the Date object.
    """
    days = {}
    month = {'01': 'янв',
             '02': 'фев',
             '03': 'мар',
             '04': 'апр',
             '05': 'май',
             '06': 'июн',
             '07': 'июл',
             '08': 'авг',
             '09': 'сен',
             '10': 'окт',
             '11': 'ноя',
             '12': 'дек'}

    def __init__(self, dt):
        """
        Initializes a Date object with a given date string.

        Args:
            dt (str): The date string in the format 'DD.MM.YYYY'.
        """
        self.__date = None
        Date.check_date(self, dt)

    @staticmethod
    def leap_year(year):
        """
        Determine if a given year is a leap year.

        Args:
            year (int): The year to be checked.

        Returns:
            dict: A dictionary containing the number of days for each month.
        """
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            Date.days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        else:
            Date.days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def check_date(self, value):
        """
        Validate the format and correctness of the date string.

        Args:
            value (str): The date string to be validated.
        """
        if not isinstance(value, str):
            print('ошибка')
            self.__date = None
        else:
            new_value = value.split('.')
            if len(new_value) > 3:
                print('ошибка')
                self.__date = None
            day = new_value[0]
            month = new_value[1]
            year = new_value[2]
            if len(day) != 2 or len(month) != 2 or len(year) != 4 or any(
                    int(i) <= 0 for i in [day, month, year]):
                print('ошибка')
                self.__date = None
            else:
                day = int(day)
                month = int(month)
                year = int(year)
                Date.leap_year(year)
                if month not in Date.days or Date.days[month] < day:
                    print('ошибка')
                    self.__date = None
                else:
                    self.__date = value

    @property
    def date(self):
        """
        Get the formatted date string.

        Returns:
            str: The formatted date string.
        """
        if self.__date is None:
            return None
        dt = self.__date.split('.')
        return f'{dt[0]} {Date.month[dt[1]]} {dt[2]}г.'

    @date.setter
    def date(self, new_dt):
        """
        Set the date from a given string.

        Args:
            new_dt (str): The new date string.
        """
        Date.check_date(self, new_dt)

    def to_timestamp(self):
        """
        Count time since 1970.

        Returns:
            int: seconds from 1970.
        """
        dt = self.__date.split('.')
        day = int(dt[0])
        month = int(dt[1])
        year = int(dt[2])
        Date.leap_year(year)
        sec_day = 86400
        sec = (day - 1) * sec_day
        for i in range(1, month):
            sec += Date.days[i] * sec_day
        for j in range(1970, year):
            Date.leap_year(j)
            for i in range(1, 13):
                sec += Date.days[i] * sec_day
        return sec

    def __eq__(self, other):
        """
        Check equality between two Date objects.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the Date objects are equal, False otherwise.
        """
        return Date.to_timestamp(self) == Date.to_timestamp(other)

    def __ne__(self, other):
        """
        Check inequality between two Date objects.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the Date objects are not equal, False otherwise.
        """
        return Date.to_timestamp(self) != Date.to_timestamp(other)

    def __lt__(self, other):
        """
        Check if one Date object is less than another.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the first Date object is less than the second, False otherwise.
        """
        return Date.to_timestamp(self) < Date.to_timestamp(other)

    def __le__(self, other):
        """
        Check if one Date object is less than or equal to another.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the first Date object is less than or equal to the second, False otherwise.
        """
        return Date.to_timestamp(self) <= Date.to_timestamp(other)

    def __gt__(self, other):
        """
        Check if one Date object is greater than another.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the first Date object is greater than the second, False otherwise.
        """
        return Date.to_timestamp(self) > Date.to_timestamp(other)

    def __ge__(self, other):
        """
         Check if one Date object is greater than or equal to another.

        Args:
            other (Date): The Date object to compare with.

        Returns:
            bool: True if the first Date object is greater than or equal to the second, False otherwise.
        """
        return Date.to_timestamp(self) >= Date.to_timestamp(other)

    def __str__(self):
        """
        Return a string representation of the Date object.

        Returns:
            str: The string representation of the Date object.
        """
        if self.__date is None:
            return 'None'
        return self.__date

    def __repr__(self):
        """
        Return a string representation of the Date object.

        Returns:
            str: The string representation of the Date object.
        """
        if self.__date is None:
            return 'None'
        return self.__date
