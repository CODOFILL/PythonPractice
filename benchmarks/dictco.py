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

def ctest(stmp, setup='pass'):
    return int(Timer(stmp, setup).timeit(number=1000000) * 1000)

t1 = ctest(
    f'deepcopy({dict_tmp})',
    r'from copy import deepcopy'
)

t2 = ctest(
    r'{i: j.copy() if isinstance(j, dict) else j for i,j in d.items()}',
    f'd = {dict_tmp}'
)

alg3 = '''
d2 = dict()
for k, v in d.items():
    if isinstance(v, dict):
        d2[k] = v.copy()
    else:
        d2[k] = v
'''

t3 = ctest(
    alg3,
    f'd = {dict_tmp}'
)


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


print(f'copy.deepcopy(x) (depth=any): {t1=} ms')
print(f'generator (depth=1): {t2=} ms')
print(f'for (depth=1): {t3=} ms')
print(f'while (depth=1): {t4=} ms')
print(f'copy.copy(x) (depth=0): {t5=} ms')
print(f'x.copy() (depth=0): {t6=} ms')