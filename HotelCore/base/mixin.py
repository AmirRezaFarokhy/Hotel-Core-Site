from datetime import datetime
import jdatetime
from django.utils import timezone


class BaseDateMixin(object):
    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M"

    def get_timestamp(self, timestamp):
        return timezone.datetime.fromtimestamp(int(timestamp))

    def convert_to_miladi(self, date):
        #  date : e.g 1375-03-15 or addable 12:12:12
        time = None
        if date.__contains__(" "):
            time = date.split(" ")[1]
            date = date.split(" ")[0]
        new_date = jdatetime.date(
            int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2])
        ).togregorian()
        value = timezone.datetime.fromisoformat(str(new_date))
        if not timezone.is_naive(value):
            value = timezone.localtime(value)
        if time:
            value = value.replace(
                hour=int(time.split(":")[0]),
                minute=int(time.split(":")[1]),
                second=int(time.split(":")[2]),
            )
        return value

    def convert_date(self, value, date_format=DATE_TIME_FORMAT, return_date=False):
        if value is None:
            return ""
        if type(value) is str:
            value = datetime.fromisoformat(value)

        if not timezone.is_naive(value):
            value = timezone.localtime(value)
        jdate = jdatetime.datetime.fromgregorian(date=value, locale="fa_IR")
        if return_date:
            return jdate
        return jdate.strftime(date_format)
    
    