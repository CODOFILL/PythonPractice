from libtool import Hamming


def run():
    h = Hamming(16)
    enc_data = h.encode(b"CODOFILL")
    print(f'{enc_data=}')
    data = h.decode(enc_data)
    print(f'{data=}')
    
    #data_bad = h.decode(b' \x00\x03\x80\x02\x83\x93G\xc4#>E\x9110\x8c')
    #print(f'{data=}')
    #print(f'{data_bad=}')


if __name__ == '__main__':
    run()