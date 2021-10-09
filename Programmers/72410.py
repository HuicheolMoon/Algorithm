# Problem : https://programmers.co.kr/learn/courses/30/lessons/72410
# Date : 2021-02-24
# 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천

import re


def solution(new_id):
    # step 1
    new_id = new_id.lower()
    # step 2
    able = re.compile("[a-z0-9-_.]")
    new_id = "".join(able.findall(new_id))
    # step 3
    series = [x for x in new_id.split(".") if x != ""]
    new_id = ".".join(series)
    # step 4
    new_id = new_id.strip(".")
    # step 5
    if len(new_id) == 0:
        new_id = "a"
    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id.rstrip(".")
    # step 7
    add_char = new_id[-1]
    while len(new_id) <= 2:
        new_id += add_char
    return new_id
