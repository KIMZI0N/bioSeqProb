# 3. 입력받은 DNA 서열에서 대문자로 변환하여 1)각 문자의 출현 빈도를 계산하고
# 2)각 뉴클레오티드를 퓨린과 피리미딘으로 나눠 그 개수를 세라.
# >> 결과값 : 각 염기의 개수를 사전형태로 출력

seq = input("dna sequence: ")
seq = seq.upper()
dic = {}
dic["A"] = seq.count("A")
dic["T"] = seq.count("T")
dic["G"] = seq.count("G")
dic["C"] = seq.count("C")
dic["Pur"] = dic["A"] + dic["G"]
dic["Pyr"] = dic["G"] + dic["C"]
print(dic)
