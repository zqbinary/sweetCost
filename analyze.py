import datetime
import dateutil.relativedelta

banks = [
    {
        'name': '招商',
        'start_day': 19,
        'internal_days': 18,
    }, {
        'name': '交通',
        'start_day': 22,
        'internal_days': 25,
    }, {
        'name': '中行',
        'start_day': 3,
        'internal_days': 20,
    }, {
        'name': '广发',
        'start_day': 17,
        'internal_days': 25,
    }, {
        'name': '花呗',
        'start_day': 10,
        'internal_days': 10,
    }
]

standardDays = 35
currentDate = datetime.date.today()
print('today', currentDate)

for bank in banks:
    bank['sweet_days'] = (bank['internal_days'] + 30) % standardDays
    bank['start_date'] = currentDate.replace(day=bank['start_day'])
    bank['end_date'] = currentDate.replace(day=bank['start_day']) \
                       + datetime.timedelta(days=bank['sweet'])
print(banks)
