from io import StringIO
import csv


def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    r1, r2, r3, r4, r5 = [], [], [], [], []

    for item in out:
        item[0] = int(item[0])
        item[1] = int(item[1])
        if item[0] not in r1:
            r1.append(item[0])
        if item[1] not in r2:
            r2.append(item[1])

    for item in out:
        for it in out:
            if item[1] == it[0]:
                if item[0] not in r3:
                    r3.append(item[0])
                if it[1] not in r4:
                    r4.append(it[1])

    for item in out:
        for it in out:
            if item[0] == it[0] and item != it:
                if item[1] not in r5:
                    r5.append(item[1])
                if it[1] not in r5:
                    r5.append(it[1])
                a, b = item[1], it[1]
                while a in r1 and b in r1:
                    for elem in out:
                        if elem[0] == a:
                            if elem[1] not in r5:
                                r5.append(elem[1])
                                a1 = elem[1]
                        if elem[0] == b:
                            if elem[1] not in r5:
                                r5.append(elem[1])
                                b1 = elem[1]
                    a, b = a1, b1

    answer = [r1, r2, r3, r4, r5]
    for mas in answer:
        mas.sort()
    return answer
