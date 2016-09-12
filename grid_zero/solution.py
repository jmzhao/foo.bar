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
    solution = solve_odd(matrix)
    if solution == None :
        return -1
    return simplify(solution).n_1()

def simplify(solution) :
    m, n = solution.dim()
    t_cross = (m + n) // 2
    t_row = n
    t_col = m
    while True :
        changed = False
        for i in range(m) :
            for j in range(n) :
                n_1 = sum([-2 * solution.at(i, j)] + solution.row(i) + solution.col(j))
                if n_1 > t_cross :
                    solution = solution.copy()
                    solution.flip_row(i)
                    solution.flip_col(j)
                    changed = True
        for i1 in range(m) :
            for i2 in range(i1+1, m) :
                n_1 = sum(solution.row(i1) + solution.row(i2))
                if n_1 > t_row :
                    solution = solution.copy()
                    solution.flip_row(i1)
                    solution.flip_row(i2)
                    changed = True
        for j1 in range(n) :
            for j2 in range(j1+1, j) :
                n_1 = sum(solution.col(j1) + solution.col(j2))
                if n_1 > t_col :
                    solution = solution.copy()
                    solution.flip_col(j1)
                    solution.flip_col(j2)
                    changed = True
        if not changed : break
    return solution

def solve_odd(matrix) :
    def has_solution(matrix) :
        m, n = matrix.dim()
        row_xors = sum(reduce(operator.xor, row) for row in matrix.rows())
        if not (row_xors == 0 or row_xors == m) : return False
        col_xors = sum(reduce(operator.xor, col) for col in matrix.cols())
        if not (col_xors == 0 or col_xors == n) : return False
        return not ((row_xors == 0) ^ (col_xors == 0))
    def strip_1(matrix) :
        return Matrix([row[:-1] for row in matrix.rows()][:-1])
    def pad_1(matrix) :
        return Matrix([row + [0] for row in itertools.chain(matrix.rows(), [[0] * matrix.dim()[1]])])

    if not has_solution(matrix) :
        return None
    reduced_matrix = strip_1(matrix)
    reduced_solution = solve_even(reduced_matrix)
    solution = pad_1(reduced_solution)
    if reduce(operator.xor, solution.row(0)) != matrix.at(0, -1) :
        solution.set(-1, -1, 1)
    return solution

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

    def set(self, i, j, v) :
        self._m[i][j] = v

    def row(self, i) :
        return list(self._m[i])

    def flip_row(self, i) :
        for j in range(len(self._m[i])) :
            self._m[i][j] = 1 - self._m[i][j]

    def col(self, j) :
        return [row[j] for row in self._m]

    def flip_col(self, j) :
        for i in range(len(self._m)) :
            self._m[i][j] = 1 - self._m[i][j]

    def rows(self) :
        for row in self._m :
            yield row

    def cols(self) :
        for col in zip(*self._m) :
            yield col

    def dim(self) :
        m = len(self._m)
        if m == 0 : return 0, 0
        return m, len(self._m[0])

    def n_1(self) :
        return sum(itertools.chain(*self._m))
