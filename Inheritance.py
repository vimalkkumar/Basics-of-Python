
class Date(object):         # Inherits the object Class
    def get_date(self):
        return "2019-05-07"


class Time(Date):           # Inherits from the Date class
    def get_time(self):
        return "07:21 AM"


date = Date()
print(date.get_date())

time = Time()
print(time.get_time(), time.get_date())     # get_date found in Date class
