def sublistas_crecientes(p):
    if p == []:
        yield []
    else:
        for x in sublistas_crecientes(p[1:]):
            if x == sorted(x):
                yield x
            if [p[0], *x] == sorted([p[0], *x]):
                yield [p[0], *x]

    