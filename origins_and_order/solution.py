import itertools

def answer(x, y, z):
    '''1 <= x, y, z <= 99'''
    valid_dates = set("%02d/%02d/%02d"%t for t in itertools.permutations([x, y, z], 3) if is_valid_date(*t))
    if len(valid_dates) == 0 :
        return "Invalid"
    elif len(valid_dates) == 1 :
        return list(valid_dates)[0]
    else :
        return "Ambiguous"

def is_valid_date(mm, dd, yy) :
    '''1 <= yy, mm, dd <= 99, no leap years'''
    return mm <= 12 and dd <= days_in_month[mm]

days_in_month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}
