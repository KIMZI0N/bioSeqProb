# 10. 이렇게 찾아진 아미노산에서 개시코돈을 확인하여 실제로 번역이 가능한 서열을 찾는 문제
# 개시코돈: AUG <- TAC. 종결아미노산: *

# base만 있는 sequence인 seq
list = []
fr = open("sequence.nucleotide.fasta", "r")
p = 0
for line in fr:
    line = line.strip()
    if p == 1:
        list.append(line)
    p = 1
seq = "".join(list)
fr.close()
