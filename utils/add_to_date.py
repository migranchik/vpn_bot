from datetime import date
from dateutil.relativedelta import relativedelta


def add_day_to_date(day_to_add: int, start_date=None) -> date:
    if start_date is None:
        start_date = date.today()
    new_date = start_date + relativedelta(days=+day_to_add)
    return new_date


def add_month_to_date(month_to_add: int, start_date=None) -> date:
    if start_date is None:
        start_date = date.today()
    new_date = start_date + relativedelta(months=+month_to_add)
    return new_date
