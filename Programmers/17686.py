# Problem : https://programmers.co.kr/learn/courses/30/lessons/17686
# Date : 2021-11-10
# 2018 KAKAO BLIND RECRUITMENT: [3차] 파일명 정렬

def solution(files):
    fileinfos = sorted([parse(file) for file in files], key=lambda x: (x[1], x[2]))
    answer = [info[0] for info in fileinfos]
    return answer


def parse(file):
    file_name = file
    head, number, tail = "", "", ""
    part = ""
    for char in file:
        if not head and char.isdigit():
            head = part
            part = char
            continue
        elif not head and not char.isdigit():
            part += char
        elif not number and char.isdigit():
            part += char
        elif not number and (not char.isdigit() or len(part) == 5):
            number = part
            part = char
            continue
        else:
            part += char
    if not number:
        number = part
    else:
        tail = part
    answer = [file_name, head.lower(), int(number), tail]
    return answer
