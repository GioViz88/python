def connectingTowns(n, routes):
    paths = 1
    for i in routes:
        paths = (paths * i) % 1234567
    return paths