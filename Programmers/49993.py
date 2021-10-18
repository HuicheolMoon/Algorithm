# Problem : https://programmers.co.kr/learn/courses/30/lessons/49993
# Date : 2021-10-19
# Summer/Winter Coding(~2018): 스킬트리

def able_tree(skill, tree):
    order = 0
    for user_skill in tree:
        if user_skill in skill:
            if skill.index(user_skill) == order:
                order += 1
            else:
                return 0
    return 1


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        answer += able_tree(skill, tree)
    return answer
