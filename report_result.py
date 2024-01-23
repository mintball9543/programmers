id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_dict = {}
    for i in range(len(report)):
        reporter, reported = report[i].split(" ")
        # print(reporter, reported)
        if reported not in report_dict:
            report_dict[reported] = set([reporter])
        else:
            report_dict[reported].add(reporter)
    # print(report_dict)
    for reported, reporters in report_dict.items():
        # print(reported, reporters)
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_list.index(reporter)] += 1
    return answer


print(solution(id_list, report, k))