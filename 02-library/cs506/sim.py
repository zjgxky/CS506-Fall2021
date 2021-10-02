def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += int(x[i]==y[i])

    if len(x) != 0:
        return 1 - res / len(x)
    else:
        return 0

def cosine_sim(x, y):
    res = 0
    lower_x = 0
    lower_y = 0
    for i in range(len(x)):
        res += x[i] * y[i]
        lower_x += x[i] ** 2
        lower_y += y[i] ** 2
    lower = lower_x ** 0.5 * lower_y ** 0.5
    if res != 0 and lower != 0:
        return res / lower
    else:
        return 0
# Feel free to add more
