import datetime, os;

ts = datetime.datetime.now().timestamp()
pid = os.getpid()
seed = ts * pid

def LCG(a, c, m):
    """Linear Congruential Generator"""
    global seed 
    while True:
        seed = (a * seed + c) % m
        yield seed

def PRNG(lower, upper):
    """Berlin Wall Pseudo Random Generator"""
    a = 1989
    c = 0
    m = 2 ** 64
    my_lcg = LCG(a, c, m)
    pick = ((upper) - lower) * (next(my_lcg) / (2 ** 64 - 1)) + lower
    return pick
