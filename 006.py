# 6. 입력받은 DNA 서열에 역상보적인 서열을 출력하라.
seq = input("dna sequence: ")
seq = seq.upper()
seqRev = seq[::-1]
seqRevCom = ""
d_base = {"A": "T", "G": "C", "C": "G", "T": "A"}
for i in seqRev:
    seqRevCom += d_base[i]
print(seqRevCom)
