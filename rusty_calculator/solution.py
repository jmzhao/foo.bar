def answer(s) :
    return parse_expr(s)

def parse_expr(expr) :
    return parse(expr, '+', parse_term)

def parse_term(term) :
    return parse(term, '*', parse_digit)

def parse_digit(digit) :
    return digit

def parse(expr, delim, subparser) :
    parts = expr.split(delim)
    return ''.join(map(subparser, parts)) + delim * (len(parts) - 1)
