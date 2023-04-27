def solution(genres, plays):
    ret = []
    genlist = {}
    for i in set(genres):
        genlist[i] = 0
    lst = [i for i in range(0,len(genres))]
    answer = list(zip(genres,plays,lst))
    answer.sort(reverse=True)
    answer.sort(reverse=True)
    reans = list(answer)
    reans.sort(key=lambda x: (-x[1], x[0], x[2]))    
    for i in reans:
        genlist[i[0]] += i[1]
    print("젠",genlist)
    genlist = sorted(genlist.items(), key=lambda x: x[1],reverse=True)
    print("순서",genlist)
    a = [i[0] for i in genlist]
    print("a = ",a)
    for i in reans:    
        print(i)
    print(reans)
    an = []
    for j in a:
        indices = [i for i, tpl in enumerate(reans) if tpl[0] == j]
        an.append(indices)
    print("an",an)
    
    for i in an:
        print(i)
        l = []
        for j in i:
            l.append(reans[j])
        print("list = ",l[0:2])
        for x in l[0:2]:
            ret.append(x[2])

    return ret
