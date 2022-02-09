# Problem : https://programmers.co.kr/learn/courses/30/lessons/43164
# Date : 2022-02-09
# 여행경로

def dfs(tickets, root):
    if not tickets:
        return [root]
    answers = []
    start = root[-1]
    for ticket in tickets:
        if ticket[0] == start:
            new_tickets = tickets[:]
            new_tickets.remove(ticket)
            new_root = root[:]
            new_root.append(ticket[-1])
            answers.extend(dfs(new_tickets, new_root))
    return answers


def solution(tickets):
    answer = sorted(dfs(tickets, ["ICN"]))[0]
    return answer
