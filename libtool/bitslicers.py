def bitslice1(data: bytes, offset: int = 1, portion: int = -1) -> int:
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


def bitslice2(data: bytes, offset: int = 1, portion: int = -1) -> int:
    
    bits_len = len(data) * 8
    offset = 1 if offset <= 0 or offset > bits_len else offset
    portion = (
        bits_len - (offset - 1)
        if portion < 0 or portion + (offset - 1) > bits_len
        else portion
    )

    bits = f'{int.from_bytes(data, "big"):0{bits_len}b}'
    return int(bits[offset - 1:(offset - 1) + portion], base=2)


def bitslice3(
        data: bytes,
        offset: int = 1,
        portion: int = -1
) -> int:
    
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