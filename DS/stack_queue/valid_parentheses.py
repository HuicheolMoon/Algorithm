# 사용자 입력에 대해 괄호 유효성을 체크하는 코드

def solution(s: str) -> bool:
    pair_dict = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in pair_dict.values():
            stack.append(char)
        elif len(stack) == 0:
            return False
        elif char in pair_dict.keys() and stack[-1] == pair_dict[char]:
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False


if __name__ == "__main__":
    s = input()
    print(solution(s))



