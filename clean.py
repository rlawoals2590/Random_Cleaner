import random
import time

li = ["정주희", "이빈", "김재민", "김정태", "김동윤", "윤현우", "유승균"]
k = int(input("오늘 오지 않은 학생의 수: "))

def random_test(random_list):
    if random_list == "정주희":
        result = "정주희 청소 당첨!"
    elif random_list == "이빈":
        result = "이빈 청소 당첨!"
    elif random_list == "김재민":
        result = "김재민 청소 당첨!"
    elif random_list == "김정태":
        result = "김정태 청소 당첨!"
    elif random_list == "김동윤":
        result = "김동윤 청소 당첨!"
    elif random_list == "윤현우":
        result = "윤현우 청소 당첨!"
    elif random_list == "유승균":
        result = "유승균 청소 당첨!"
    return result

if k == 0:
    test = random_test(random.choice(li))
    alist = []
    for i in range(3):
        while test in alist:
            test = random_test(random.choice(li))
        alist.append(test)
        print(test)
        time_duration = 0.5
        time.sleep(time_duration)
    time_duration = 10
    time.sleep(time_duration)
elif k == 1:
    a = str(input("오늘 오지 않은 학생의 이름: "))
    li.remove(str(f"{a}"))
    test = random_test(random.choice(li))
    alist = []
    for i in range(3):
        while test in alist:
            test = random_test(random.choice(li))
        alist.append(test)
        print(test)
        time_duration = 0.5
        time.sleep(time_duration)
    time_duration = 10
    time.sleep(time_duration)
elif k == 2:
    b, c = input("오늘 오지 않은 학생의 이름: ").split()
    li.remove(str(f'{b}'))
    li.remove(str(f'{c}'))
    test = random_test(random.choice(li))
    alist = []
    for i in range(3):
        while test in alist:
            test = random_test(random.choice(li))
        alist.append(test)
        print(test)
        time_duration = 0.5
        time.sleep(time_duration)
    time_duration = 10
    time.sleep(time_duration)
elif k == 3:
    d, e, f = input("오늘 오지 않은 학생의 번호: ").split()
    li.remove(str(f'{d}'))
    li.remove(str(f'{e}'))
    li.remove(str(f'{f}'))
    test = random_test(random.choice(li))
    alist = []
    for i in range(3):
        while test in alist:
            test = random_test(random.choice(li))
        alist.append(test)
        print(test)
        time_duration = 0.5
        time.sleep(time_duration)
    time_duration = 10
    time.sleep(time_duration)