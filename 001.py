# 1. 입력받은 DNA서열의 길이와 유효한 문자들을 센 값이 서로 같은지 확인하여 전체 서열이 유효한 문자를 가지고 있는지 확인한다.
# >> 결과값 : 유효하면 True, 유효하지 않으면 False

seq = input("dna sequence: ")
seq = seq.upper()

A = seq.count("A")
T = seq.count("T")
G = seq.count("G")
C = seq.count("C")

if len(seq) == (A + T + G + C):
    print(True)
else:
    print(False)
