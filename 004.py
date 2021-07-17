# 입력받은 DNA서열에서 GC 함량을 계산하라.
# >> 결과값 :　GC %
seq = input("dna sequence: ")
seq = seq.upper()

G = seq.count("G")
C = seq.count("C")
res = (G + C) / len(seq) * 100
print(res, "%")
