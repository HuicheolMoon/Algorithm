# Problem : https://programmers.co.kr/learn/courses/30/lessons/67256
# Date : 2021-02-24
# 2020 카카오 인턴십 키패드 누르기

def solution(numbers, hand):
    answer = ""
    # 왼손, 오른손의 초기 좌표 (1 버튼이 (0,0))
    L_position = [3, 0]
    R_position = [3, 2]
    for number in numbers:
        if number in [1, 4, 7]:
            # 왼쪽 버튼들은 왼손으로
            use = "left"
        elif number in [3, 6, 9]:
            # 오른쪽 버튼들은 오른손으로
            use = "right"
        else:
            if number == 0:
                number = 11
            # 왼손과 오른손의 현재 좌표에 대한 버튼의 거리 계산
            L_distance = abs((number - 1) // 3 - L_position[0]) + abs(((number - 1) % 3 - L_position[1]))
            R_distance = abs((number-1) // 3 - R_position[0]) + abs(R_position[1] - ((number - 1) % 3))
            if L_distance == R_distance:
                use = hand
            elif L_distance < R_distance:
                use = "left"
            else:
                use = "right"
        # 계산한 결과를 answer에 저장하고 사용한 손의 좌표 이동
        if use == "left":
            answer += "L"
            L_position = [((number - 1) // 3), ((number - 1) % 3)]
        elif use == "right":
            answer += "R"
            R_position = [((number - 1) // 3), ((number - 1) % 3)]
    return answer
