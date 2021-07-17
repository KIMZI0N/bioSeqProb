# 2. 입력받은 DNA 서열이 이의 상보적 서열과 같은지 확인하라.(Palindromic sequence?)
seq = input("dna sequence: ")
seq = seq.upper()
seqRev = seq[::-1]
seqCom = ""
d_base = {"A": "T", "G": "C", "C": "G", "T": "A"}
for i in seq:
    seqCom += d_base[i]
if seqCom == seqRev:
    print("Palindromic sequence")
else:
    print("Unpalindromic sequence")
