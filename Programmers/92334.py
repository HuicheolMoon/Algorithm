# Problem : https://programmers.co.kr/learn/courses/30/lessons/92334
# Date : 2022-02-09
# 2022 KAKAO BLIND RECRUITMENT: 신고 결과 받기

def solution(id_list, report, k):
    user_info = dict()
    for user in id_list:
        user_info[user] = [set([]), 0] #[유저가 신고한 타 유저, 유저가 신고당한 횟수]
    for rep in report:
        rep_comp, rep_def = rep.split()
        if rep_def not in user_info[rep_comp][0]:
            user_info[rep_comp][0].add(rep_def)
            user_info[rep_def][1] += 1
    banned_users = set() #정지당한 유저 리스트
    for info in user_info.items():
        if info[1][1] >= k:
            banned_users.add(info[0])
    result_mails = [] #결과 메일을 받은 횟수 리스트
    for user in id_list:
        num_mail = len(user_info[user][0] & banned_users)
        result_mails.append(num_mail)
    return result_mails
