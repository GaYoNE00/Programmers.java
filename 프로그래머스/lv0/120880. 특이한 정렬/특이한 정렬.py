def solution(numlist, n):
    answer = []
    numlist.sort(reverse = True)
    repare = list(numlist)
    for i in range(len(numlist)):
        print(i)
        a = numlist[0]
        for j in range(len(numlist)):
            if abs(n-numlist[j]) < abs(n-a):
                a = numlist[j]
        print(a)
        i = i-1
        numlist.remove(a)
        answer.append(a)


    return answer