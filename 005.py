# 5. 입력받은 DNA 서열의 전사한 RNA 서열을 출력하라.
seq = input("dna sequence: ")
seq = seq.upper()
seqCom = ""
d_base = {"A": "U", "G": "C", "C": "G", "T": "A"}
for i in seq:
    seqCom += d_base[i]
print(seqCom)
