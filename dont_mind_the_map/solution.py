import itertools

def answer(subway):
    subway = Subway(subway)
    if subway.has_meeting_path() : return -1
    for station in subway.stations() :
        if subway.close(station).has_meeting_path() : return station
    return -2

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
        def calc_ultimate(acc, f) :
            return reduce(compose, all_possible_func_combinations(acc, f, n_stations))
        ultimate_func = reduce(calc_ultimate, funcs, Function(enumerate(range(n_stations))))
        # print("ultimate_func:")
        # print(str(ultimate_func))
        return ultimate_func.is_constant()

def compose(f1, f2) :
    return f1.compose(f2)

def all_possible_func_combinations(f1, f2, n_max) :
    for f1i, f2i in itertools.product([f1.power(i) for i in range(n_max)], [f2.power(i) for i in range(n_max)]) :
        yield f1i
        yield f2i

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
