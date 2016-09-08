import operator
import copy
import itertools

def answer(matrix) :
    matrix = Matrix(matrix)
    n, _ = matrix.dim()
    ## unique solution when n is even
    if n % 2 == 0 :
        return solve_even(matrix).n_1()
    ## possibly multiple or no solution when n is odd
    try :
        return min(sol.n_1() for sol in solve_odd(matrix))
    except ValueError :
        ## if no solution
        return -1

def solve_odd(matrix) :
    '''gives back a generator of possible solution(s)'''
    def is_true_solution(ps) :
        return all(map(lambda x : x == 0, ps.row(-1) + ps.col(-1)))
    def to_true_solution(ps) :
        return Matrix([row[:-1] for row in ps.getArray()[:-1]])
    m, n = matrix.dim()
    a = matrix.getArray()
    for i in range(m) :
        a[i].append(0)
    a.append([0] * (n + 1))
    for new_col in itertools.product((0, 1), repeat=m) :
        for i in range(m) : a[i][n] = new_col[i]
        for new_row in itertools.product((0, 1), repeat=n+1) :
            a[m] = list(new_row)
            potential_solution = solve_even(Matrix(a))
            if is_true_solution(potential_solution) :
                yield to_true_solution(potential_solution)

def solve_even(matrix) :
    '''gives back the unique solution'''
    m, n = matrix.dim()
    return Matrix([[
        reduce(operator.xor, [matrix.at(i, j)] + matrix.row(i) + matrix.col(j))
            for j in range(n)]
        for i in range(m)])

class Matrix :
    def __init__(self, m) :
        self._m = copy.deepcopy(m)

    def copy(self) :
        return Matrix(self._m)

    def getArray(self) :
        return copy.deepcopy(self._m)

    def at(self, i, j) :
        return self._m[i][j]

    def row(self, i) :
        return list(self._m[i])

    def col(self, j) :
        return [row[j] for row in self._m]

    def dim(self) :
        return len(self._m), len(self._m[0])

    def n_1(self) :
        return sum(itertools.chain(*self._m))
