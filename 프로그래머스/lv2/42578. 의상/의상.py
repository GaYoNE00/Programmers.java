def solution(clothes):
    fashion = {}    
    for i in clothes:
        if i[1] not in fashion.keys():
            fashion[i[1]] = 1
        else:
            fashion[i[1]] += 1
    answer = 1
    for k,v in fashion.items():
        answer = answer*(v+1)
    return answer-1
