# Problem : https://programmers.co.kr/learn/courses/30/lessons/17677
# Date : 2021-09-03
# 2018 KAKAO BLIND RECRUITMENT [1차] 뉴스 클러스터링

from collections import Counter


def solution(str1, str2):
    set1 = []
    set2 = []
    for i in range(len(str1) - 1):
        part = str1[i:i+2]
        if part.isalpha():
            set1.append(part.lower())
    for j in range(len(str2) - 1):
        part = str2[j:j+2]
        if part.isalpha():
            set2.append(part.lower())
    c1 = Counter(set1)
    c2 = Counter(set2)
    n_interset = len(list((c1 & c2).elements()))
    n_unionset = len(list((c1 | c2).elements()))
    if n_unionset == 0:
        jaccard = 1
    else:
        jaccard = n_interset / n_unionset
    return int(jaccard * 65536)
