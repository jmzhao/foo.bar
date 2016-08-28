def log(f) :
    def decorated(*args) :
        print("Call %s(%s)"%(f.__name__, ', '.join(map(str, args))))
        res = f(*args)
        print("%s(%s) => %s"%(f.__name__, ', '.join(map(str, args)), res))
        return res
    return decorated

def cached(f) :
    cache = dict()
    def decorated(*args) :
        return cache.setdefault(args, f(*args))
    return decorated
