from timeit import Timer

dict_tmp = {
    'u': 0,
    'z': 0,
    'x': 1,
    'y': {
        'x': 1,
        'y': 2
    },
    't': 0
}

alg3 = '''
d2 = dict()
for k, v in d.items():
    if isinstance(v, dict):
        d2[k] = v.copy()
    else:
        d2[k] = v
'''

alg4 = '''
d2 = dict()
l = list(d.items())
i = 0 
while i < len(l):
    if isinstance(l[i][1], dict):
        d2[l[i][0]] = l[i][1].copy()
    else:
        d2[l[i][0]] = l[i][1]
    i += 1
'''


def ctest(stmp, setup='pass'):
    return int(Timer(stmp, setup).timeit(number=1000000) * 1000)


def run():
    print(f'1M dict copy begin...')
    t1 = ctest(
        f'deepcopy({dict_tmp})',
        r'from copy import deepcopy'
    )

    t2 = ctest(
        r'{i: j.copy() if isinstance(j, dict) else j for i,j in d.items()}',
        f'd = {dict_tmp}'
    )

    t3 = ctest(
        alg3,
        f'd = {dict_tmp}'
    )

    t4 = ctest(
        alg4,
        f'd = {dict_tmp}'
    )

    t5 = ctest(
        f'x = copy({dict_tmp})',
        r'from copy import copy'
    )

    t6 = ctest(
        f'x = {dict_tmp}.copy()'
    )

    print(f't1: {t1:<4d} ms -> copy.deepcopy(x) (depth=1 of any)')
    print(f't2: {t2:<4d} ms -> generator (depth=1)')
    print(f't3: {t3:<4d} ms -> for (depth=1)')
    print(f't4: {t4:<4d} ms -> while (depth=1)')
    print(f't5: {t5:<4d} ms -> copy.copy(x) (depth=0)')
    print(f't6: {t6:<4d} ms -> x.copy() (depth=0)')