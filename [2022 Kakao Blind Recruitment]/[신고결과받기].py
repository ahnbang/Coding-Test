def solution(id_list, report, k):
    report =set(report)
    answer = [0]*len(id_list)
    count=[0]*len(id_list)
    dic ={}
    for i in id_list:
        dic[i] = []
    
    for i in report:
        report = i.split()
        if dic[report[0]] != [report[1]]: 
            dic[report[0]].append(report[1])

    for i in range(len(id_list)):
        id_list[i]
        for ID in id_list:
            if id_list[i] in dic[ID]:
                count[i]+=1

    for i in range(len(id_list)):
        if count[i] >= k:
            for j in range(len(id_list)):
                if id_list[i] in dic[id_list[j]]:
                    answer[j]+=1
    return answer
