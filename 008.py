# 8. 주어진 아미노산을 암호화하고 있는 각 코돈의 비율을 DNA 서열로 표현
# 결과를 사전으로 반환하며 사전의 키는 코돈이고 값은 코돈의 사용빈도를 나타낸다.
d_codon = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
seq = input("dna sequence: ")
inAmi = input("amino acid: ")  # input amino acid
# 딕셔너리로 하면 count를 1까지밖에 못 셈! 딕셔너리의 key값이 유일해야 하므로..?
l_cod = []
l_ami = []

for i in range(0, len(seq), 3):
    s = seq[i : i + 3]
    l_cod.append(s)  # input sequence를 codon단위로 list에 저장
    l_ami.append(d_codon[s])  # l_cod과 매칭되는 아미노산을 list에 저장
# print(l_cod)
# print(l_ami)

d_res = {}  # result를 담는 dictionary. key: codon, value: count

for i in range(len(l_ami)):
    if l_ami[i] == inAmi:  # inAmi가 있는 list의 index를 i라 하자. ex) i = 5, 6, 7, 8, 9
        cod = l_cod[i]
        # 같은 index인 codon list값을 cod에 저장. ex) GGG, GGA, GGC, GGT, GGT
        if cod in d_res:  # cod가 결과 딕셔너리에 있으면 +1
            d_res[cod] += 1
        else:  # 없으면 1 저장.
            d_res[cod] = 1

print(d_res)
# result
# $ python 008.py
# dna sequence: ACACAGACTCCCCACGGGGGAGGCGGTGGT
# amino acid: G
# {'GGG': 1, 'GGA': 1, 'GGC': 1, 'GGT': 2}

# value로 key 찾기!
# for key, val in d_trans.items():
#     if val == inAmi:
#         print(key)
