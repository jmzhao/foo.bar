from fractions import gcd

class Vector :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def minus(self, v) :
        return Vector(self.x - v.x, self.y - v.y)

    def __str__(self) :
        return "Vector(%d, %d)"%(self.x, self.y)

def answer(vertices):
    triangle = [Vector(*l) for l in vertices]
    return n_integer_points_in_triangle(*triangle)

def n_integer_points_in_triangle(p, q, r) :
    return area_triangle(p, q, r) - n_integer_points_along_triangle(p, q, r) / 2 + 1

def area_triangle(p, q, r) :
    p = p.minus(r)
    q = q.minus(r)
    return abs(p.x * q.y - p.y * q.x) / 2

def n_integer_points_along_triangle(p, q, r) :
    return sum(n_integer_points_in_line(v) for v in (p.minus(q), q.minus(r), r.minus(p)))

def n_integer_points_in_line(v) :
    return abs(gcd(v.x, v.y))
