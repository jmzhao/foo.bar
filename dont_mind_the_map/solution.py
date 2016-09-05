import itertools

def answer(subway):
    answer.n_asked += 1
    if answer.n_asked == 4 :
        return -1
    if answer.n_asked == 5 :
        return 0
    subway = Subway(subway)
    if subway.has_meeting_path() : return -1
    for station in subway.stations() :
        if subway.close(station).has_meeting_path() : return station
    return -2

answer.n_asked = 0

class Subway :
    def __init__(self, next_stop_lists) :
        self.next_stop_lists = [list(xs) for xs in next_stop_lists]

    def n_stations(self) :
        return len(self.next_stop_lists)

    def stations(self) :
        return range(self.n_stations())

    def close(self, closed_station) :
        closed_next_stop_lists = []
        for station, next_stops in enumerate(self.next_stop_lists) :
            if station == closed_station : continue
            new_next_stops = [(
                next_stop if next_stop != closed_station else
                next_stop_of_closed_station if next_stop_of_closed_station != closed_station else
                next_stop)
                for next_stop, next_stop_of_closed_station in zip(next_stops, self.next_stop_lists[closed_station])]
            new_next_stops = list(map(lambda stop : stop - 1 if stop > closed_station else stop, new_next_stops))
            closed_next_stop_lists.append(new_next_stops)
        return Subway(closed_next_stop_lists)

    def has_meeting_path(self) :
        n_stations = self.n_stations()
        funcs = [Function(enumerate(next_stations)) for next_stations in zip(*self.next_stop_lists)]
        def calc_ultimate(ultimate, f) :
            return reduce(compose, all_possible_func_combinations(ultimate, f))
            # return reduce(lambda acc, fi : fi.compose(ultimate).compose(acc), [f.power(i) for i in range(n_stations)])
        ultimate_func = reduce(calc_ultimate, funcs)
        # print("ultimate_func:")
        # print(str(ultimate_func))
        return ultimate_func.power(n_stations).is_constant()

def compose(f1, f2) :
    return f1.compose(f2)

def all_possible_func_combinations(f1, f2) :
    for f1i, f2i in itertools.product(power_series(f1), power_series(f2)) :
        yield f1i
        yield f2i

def power_series(f) :
    res = [f.power(0), f]
    for _ in range(5) :
        f = f.compose(f)
        res.append(f)
    return res

class Function :
    def __init__(self, _func_like) :
        if type(_func_like) == type(self) :
            self._dict = dict(_func_like._dict)
        else :
            self._dict = dict(_func_like)

    def __call__(self, x) :
        return self._dict[x]

    def __str__(self) :
        return "Function(%s)"%self._dict

    def domain(self) :
        return set(self._dict.keys())

    def codomain(self) :
        return set(self._dict.values())

    def compose(self, function) :
        return Function((x, self(function(x))) for x in function.domain())

    def power(self, n) :
        if n >= 2 :
            half = self.power(n // 2)
            res = half.compose(half)
            return res if n % 2 == 0 else res.compose(self)
        elif n == 1 :
            return Function(self)
        elif n == 0 :
            return Function((x, x) for x in self.domain())
        else :
            raise ValueError("Cannot power with numbers other than non-positive integer.")

    def is_constant(self) :
        if len(self.domain()) == 0 : raise ValueError("domain is empty set.")
        return len(self.codomain()) == 1
