from collections import defaultdict


def solution(id_list, report, k):
    black_list = defaultdict(set)
    users = dict.fromkeys(id_list, 0)

    for s in report:
        l, r = s.split()
        black_list[r].add(l)

    for ids in black_list.values():
        if len(ids) < k:
            continue
        for _id in ids:
            users[_id] += 1

    return list(users.values())


if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k))
