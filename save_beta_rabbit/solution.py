def answer(food, grid):
    costs = all_possible_cost(grid)
    try :
        m = max(x for x in costs if x <= food)
    except ValueError :
        return -1
    return food - m

def all_possible_cost(grid) :
    n = len(grid)
    a = [[set() for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if i == 0 :
                if j == 0 :
                    a[i][j] = set([0])
                else :
                    a[i][j] = set(x + grid[i][j] for x in a[i][j-1])
            else :
                if j == 0 :
                    a[i][j] = set(x + grid[i][j] for x in a[i-1][j])
                else :
                    a[i][j] = set(x + grid[i][j] for x in a[i-1][j] | a[i][j-1])
    return a[n-1][n-1]
