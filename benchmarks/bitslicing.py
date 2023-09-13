import timeit


BENCH_INFO = '''
For example data is 'Hello!' encoded of utf-8:
01001000 01100101 01101100
01101100 01101111 00100001

offset=11, portion=10
return: 0b1001010110
'''

BENCH_SETUP = '''
from libtool import (
    bitslice1,
    bitslice2,
    bitslice3,
)
d = bytes('Hello!', 'utf-8')
'''

def run():
    print(
        f'{BENCH_INFO}\n'
        f'{BENCH_SETUP}\n'
        '\n1M bitsliceN(d, 11, 10) begin...'
    )
    t1 = timeit.timeit(
        'bitslice1(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )
    t2 = timeit.timeit(
        'bitslice2(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )
    t3 = timeit.timeit(
        'bitslice3(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )

    print(
        f'bitslice1: {t1:.2f} sec\n'
        f'bitslice2: {t2:.2f} sec\n'
        f'bitslice3: {t3:.2f} sec'
    )