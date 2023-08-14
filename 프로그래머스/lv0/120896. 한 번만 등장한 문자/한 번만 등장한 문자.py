def solution(s):
    answer = ''
    a = sorted(set(s), reverse=False)
    for i in a:
        if s.count(i) == 1:
            answer = answer+i
    return answer
