# Problem : https://programmers.co.kr/learn/courses/30/lessons/42888
# Date : 2021-09-03
# 2019 KAKAO BLIND RECRUITMENT - 오픈채팅방

def solution(record):
    answer = []
    seq = []
    users = dict()
    for rec in record:
        q = rec.split()
        if q[0] == "Enter":
            users[q[1]] = q[2]
            seq.append([q[0], q[1]])
        elif q[0] == "Change":
            users[q[1]] = q[2]
        else:
            seq.append([q[0], q[1]])
    for query in seq:
        op, user_name = query[0], users[query[1]]
        if op == "Enter":
            sent = f"{user_name}님이 들어왔습니다."
        elif op == "Leave":
            sent = f"{user_name}님이 나갔습니다."
        answer.append(sent)
    return answer
