import datetime
import dateutil.relativedelta

"""
/**
 *     [
 * 'name' : '招商',
 * //个人数据：账单日
 * 'start_day' : 19,
 * //银行数据：
 * 'internal_days' : 18,
 * ],
 */
 """
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

msg = '推荐用卡次序为：'
currentDate = datetime.date.today()

print('today', currentDate)
today = currentDate.strftime("%d")
longOrder = {}
for bank in banks:
    # 下个月 前一天是截止日
    if int(today) >= bank['start_day']:
        bank['start_date'] = currentDate.replace(day=bank['start_day'])
        bank['end_date'] = currentDate.replace(day=bank['start_day']) \
                           - datetime.timedelta(days=1) \
                           + dateutil.relativedelta.relativedelta(months=1)
    else:
        bank['start_date'] = currentDate.replace(day=bank['start_day']) \
                             + dateutil.relativedelta.relativedelta(months=-1)
        bank['end_date'] = currentDate.replace(day=bank['start_day']) \
                           - datetime.timedelta(days=1)
    bank['repay_date'] = bank['end_date'] + datetime.timedelta(days=int(bank['internal_days']) + 1)
    bank['repay_interval'] = int((bank['repay_date'] - currentDate).days)
    for dateStr in ['start_date', 'end_date', 'repay_date']:
        bank[dateStr] = bank[dateStr].strftime("%m%d")
    # print(item)
#
banks.sort(key=lambda k: k['repay_interval'], reverse=True)
for bank in banks:
    msg += '\r\n' + str(bank['repay_interval']) + "天后【" + bank['name'] + '】于:' + bank['repay_date']
print(msg)
