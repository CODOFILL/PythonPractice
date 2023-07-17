import timeit

# For example 'data' is 'Hello!' encoded of 'utf-8':
# 01001000 01100101 01101100
# 01101100 01101111 00100001
# For offset=11, portion=10
# return: 0b1001010110

BENCH_SETUP = '''
from benchmarks.bitslicers import (
    bitslicer1,
    bitslicer2,
    bitslicer3,
)
d = bytes('Hello!', 'utf-8')
'''


def bitslicer1(data: bytes, offset: int = 1, portion: int = -1) -> int:
    bytes_data = bytearray(data)
    
    bits_len = len(data) * 8
    offset = 1 if offset <= 0 or offset > bits_len else offset
    portion = (
        bits_len - (offset - 1)
        if portion < 0 or portion + (offset - 1) > bits_len
        else portion
    )

    res = 0
    for i in range(portion):
        byte = bytes_data[((offset + i) - 1) // 8]
        bit_pos = (((offset + i) - 1) % 8) + 1
        bit_val = int(bool(byte & (2 ** 8 >> bit_pos)))
        res = (res << 1) + bit_val
    return res 


def bitslicer2(data: bytes, offset: int = 1, portion: int = -1) -> int:
    
    bits_len = len(data) * 8
    offset = 1 if offset <= 0 or offset > bits_len else offset
    portion = (
        bits_len - (offset - 1)
        if portion < 0 or portion + (offset - 1) > bits_len
        else portion
    )

    bits = f'{int.from_bytes(data, "big"):0{bits_len}b}'
    return int(bits[offset - 1:(offset - 1) + portion], base=2)


def bitslicer3(data: bytes, offset: int = 1, portion: int = -1) -> int:
    
    bits_len = len(data) * 8
    data = int.from_bytes(bytes(data), 'big')

    offset = 1 if offset <= 0 or offset > bits_len else offset
    portion = (
        bits_len - (offset - 1)
        if portion < 0 or portion + (offset - 1) > bits_len
        else portion
    )

    mask = (2 ** (bits_len - (offset - 1))) - 1
    shift = bits_len - offset - (portion - 1)
    return (data & mask ) >> shift


def bench():
    t1 = timeit.timeit(
        'bitslicer1(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )
    t2 = timeit.timeit(
        'bitslicer2(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )
    t3 = timeit.timeit(
        'bitslicer3(d, 11, 10)',
        BENCH_SETUP,
        number = 1000000
    )
   
    print(f'{t1=}\n{t2=}\n{t3=}')


if __name__ == '__main__':
    d = bytes('Hello!', 'utf-8')
    print(f'{bitslicer1(d, 11, 10):010b}')
    print(f'{bitslicer2(d, 11, 10):010b}')
    print(f'{bitslicer3(d, 11, 10):010b}')
