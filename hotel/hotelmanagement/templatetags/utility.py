from django import template

register = template.Library()

@register.filter(name='get_length')
def _get_length(value):
    return value.count

@register.filter(name='auto_range')
def _auto_range(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    args = filter(None, (_min, _max, _step))
    return range(*args)

@register.filter(name='get_cash_rate')
def _get_cash_rate(arr, booking_id):
    lst = []
    for item in arr:
        if item[6] == 1 and item[5] == booking_id:
            lst.append(item)

    return lst


@register.filter(name='get_credit_rate')
def _get_credit_rate(arr, booking_id):
    lst = []
    for item in arr:
        if item[6] == 2 and item[5] == booking_id:
            lst.append(item)

    return lst

@register.filter(name='get_bank_rate')
def _get_bank_rate(arr, booking_id):
    lst = []
    for item in arr:
        if item[6] == 3 and item[5] == booking_id:
            lst.append(item)

    return lst

@register.filter(name='get_by_index')
def _get_by_index(arr, index):
    if len(arr) == 0:
        return ''
    try:
        return arr[index][1]
    except:
        return ''


@register.filter(name='get_deposit')
def _get_deposit(arr, index):
    if len(arr) == 0:
        return ''
    try:
        if arr[index][4] is True:
            return 'Yes'
        return ''
    except:
        return ''
