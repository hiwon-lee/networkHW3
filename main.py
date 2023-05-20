def crc_shift_register(data, generator) :
    # 문자열을 리스트로 받았습니다.
    data = list(map(int, data.split()))
    generator = list(map(int, generator.split()))

    info = data+[0]*(len(generator)-1)
    crc = info[0:len(generator)-1]

    #shift register 방식으로 crc를 구하는 코드를 작성해주세요
    for i in range(len(data)) :
        if crc[0] == 0 :
            crc.append(info[i+len(crc)])
            crc.pop(0)
        else :
            crc.append(info[i+len(crc)])
            crc.pop(0)
            crc = list_xor(crc, generator[1::])


    # crc = info[len(data):];
    codeword = data + crc;


    #crc : CRC bits
    #codeword : <data, crc>
    return crc, codeword

def list_xor(a,b):
    c = [0]*len(a)
    for i in range(len(a)) :
        c[i] = a[i] ^ b[i]
    return c

def crc_check(codeword, generator) :
    # 조건에 맞게 error 여부 출력
    # 문자열을 리스트로 받았습니다.
    codeword = list(map(int, codeword.split()))
    generator = list(map(int, generator.split()))

    # info = data + [0] * (len(generator) - 1)
    crc = codeword[0:len(generator) - 1]

    # shift register 방식으로 crc를 구하는 코드를 작성해주세요
    for i in range(len(codeword)-len(crc)):
        if crc[0] == 0:
            crc.append(codeword[i + len(crc)])
            crc.pop(0)
        else:
            crc.append(codeword[i + len(crc)])
            crc.pop(0)
            crc = list_xor(crc, generator[1::])
    # error 있을 때 : "An error is detected (according to CCITT-16)!"
    # error 없을 때 : "An error is not detected (according to CCITT-16)!"
    if 1 in crc :
        print("An error is detected (according to CCITT-{})!".format(len(crc)))
    else :
        print("An error is not detected (according to CCITT-{})!".format(len(crc)))



def hw3_part2() :
    print("[HW #3 Part II] student ID: {} Name: {}".format("2171087", "HeeWon LEe"))
    mode = input("Select the mode between TX and RX (TX:1, RX:2): ")

    if mode == "1":
        data = input("Type information bits that you want to send ex) 1 0 0 1 0 1:")
        generator = input("Type generator bits: ")
        crc, codeword = crc_shift_register(data,generator)
        print("CRC bits calculated by CCITT-{}:".format(len(crc)), crc)
        print("The complete codeword:", codeword)
        print("Done...")

    elif mode == "2":
        codeword = input("Type the codeword that RX received: ex) x x x ... x x: ")
        generator = input("Type generator bits: ")
        crc_check(codeword, generator)
        print("Done...")

    else:
        print("select 1 or 2 again.")
if __name__ == '__main__':
    hw3_part2()

