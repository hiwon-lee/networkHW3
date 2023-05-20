def crc_shift_register(data, generator) :
    # 문자열을 리스트로 받았습니다.
    data = list(map(int, data.split()))
    generator = list(map(int, generator.split()))

    # shift_register에 넣을 codeword(여기서는 변수를 info로 둠)와 crc를 만듭니다
    info = data+[0]*(len(generator)-1)
    # crc의 길이는 generator길이보다 1작으며, shift_register의 시작은 모든 원소가 0이므로, codeword의 crc길이만큼 해당되는 앞부분은 변화없이 register에 들어갑니다.
    crc = info[0:len(generator)-1]

    #shift register 방식으로 crc를 구하는 코드를 작성해주세요
    # codeword에서 crc길이만큼 뺀 나머지 부분만큼 연산을 진행 (왜냐하면, 초기 crc에 codeword앞부분을 미리 다 넣어 둠)
    for i in range(len(data)) :
        if crc[0] == 0 : # crc[0]이 0 인 경우, xor을 계산을 해도 변화가 없으므로 codeword의 다음 성분을 추가하고, crc의 앞부분은 없앤다.
            crc.append(info[i+len(crc)])
            crc.pop(0)
        else : # crc[0]이 1 인 경우, xor 계산을 진행한다.
            crc.append(info[i+len(crc)])
            crc.pop(0)
            crc = list_xor(crc, generator[1::]) #generator[0]은 shift할 때, 연산에 관여하지 않으므로 인덱스 1부터 xor연산을 진행한다.


    #codeword를 만든다.
    codeword = data + crc;


    #crc : CRC bits
    #codeword : <data, crc>
    return crc, codeword

def list_xor(a,b):
    c = [0]*len(a) #최종적으로 반환할 연산의 초기값을 설정
    for i in range(len(a)) : #xor연산을 하여 c에 저장
        c[i] = a[i] ^ b[i]
    return c

def crc_check(codeword, generator) :
    # 조건에 맞게 error 여부 출력
    # 문자열을 리스트로 받았습니다.
    codeword = list(map(int, codeword.split()))
    generator = list(map(int, generator.split()))

    # codeword의 앞부분은 0과 xor연산을 진행하므로 값에 변화가 없기 때문에, crc길이에 해당하는 codeword의 앞부분은 바로 crc로 넣어준다.
    crc = codeword[0:len(generator) - 1]

    # shift register 방식으로 crc를 구하는 코드를 작성해주세요
    for i in range(len(codeword)-len(crc)): #codeword에서 이미 register에 들어간 부분(crc길이만큼)을 빼준 길이 만큼 shift register를 돌려준다.
        if crc[0] == 0: # crc[0]이 0 인 경우, xor을 계산을 해도 변화가 없으므로 codeword의 다음 성분을 추가하고, crc의 앞부분은 없앤다.
            crc.append(codeword[i + len(crc)])
            crc.pop(0)
        else: # crc[0]이 1 인 경우, xor 계산을 진행한다.
            crc.append(codeword[i + len(crc)])
            crc.pop(0)
            crc = list_xor(crc, generator[1::]) #generator[0]은 shift할 때, 연산에 관여하지 않으므로 인덱스 1부터 xor연산을 진행한다.

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

