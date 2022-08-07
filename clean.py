import random
import time

li = [1, 2, 3, 4, 5, 6, 7]
k = int(input("오늘 오지 않은 학생의 수: "))
if k == 0:
    alist = []
    for i in range(3):
        random_num = random.choice(li)
        while random_num in alist:
            random_num = random.choice(li)
        alist.append(random_num)
        if random_num == 1:
            print("정주희 청소 당첨!")
        elif random_num == 2:
            print("이빈 청소 당첨!")
        elif random_num == 3:
            print("김재민 청소 당첨!")
        elif random_num == 4:
            print("김정태 청소 당첨!")
        elif random_num == 5:
            print("김동윤 청소 당첨!")
        elif random_num == 6:
            print("윤현우 청소 당첨!")
        elif random_num == 7:
            print("유승균 청소 당첨!")
    time_duration = 10
    time.sleep(time_duration)
elif k == 1:
    a = int(input("오늘 오지 않은 학생의 번호: "))
    li.remove(a)
    alist = []
    for i in range(3):
        random_num = random.choice(li)
        while random_num in alist:
            random_num = random.choice(li)
        alist.append(random_num)
        if random_num == 1:
            print("정주희 청소 당첨!")
        elif random_num == 2:
            print("이빈 청소 당첨!")
        elif random_num == 3:
            print("김재민 청소 당첨!")
        elif random_num == 4:
            print("김정태 청소 당첨!")
        elif random_num == 5:
            print("김동윤 청소 당첨!")
        elif random_num == 6:
            print("윤현우 청소 당첨!")
        elif random_num == 7:
            print("유승균 청소 당첨!")
    time_duration = 10
    time.sleep(time_duration)
elif k == 2:
    b, c = map(int, input("오늘 오지 않은 학생의 번호: ").split())
    li.remove(b)
    li.remove(c)
    alist = []
    for i in range(3):
        random_num = random.choice(li)
        while random_num in alist:
            random_num = random.choice(li)
        alist.append(random_num)
        if random_num == 1:
            print("정주희 청소 당첨!")
        elif random_num == 2:
            print("이빈 청소 당첨!")
        elif random_num == 3:
            print("김재민 청소 당첨!")
        elif random_num == 4:
            print("김정태 청소 당첨!")
        elif random_num == 5:
            print("김동윤 청소 당첨!")
        elif random_num == 6:
            print("윤현우 청소 당첨!")
        elif random_num == 7:
            print("유승균 청소 당첨!")
    time_duration = 10
    time.sleep(time_duration)
elif k == 3:
    d, e, f = map(int, input("오늘 오지 않은 학생의 번호: ").split())
    li.remove(d)
    li.remove(e)
    li.remove(f)
    alist = []
    for i in range(3):
        random_num = random.choice(li)
        while random_num in alist:
            random_num = random.choice(li)
        alist.append(random_num)
        if random_num == 1:
            print("정주희 청소 당첨!")
        elif random_num == 2:
            print("이빈 청소 당첨!")
        elif random_num == 3:
            print("김재민 청소 당첨!")
        elif random_num == 4:
            print("김정태 청소 당첨!")
        elif random_num == 5:
            print("김동윤 청소 당첨!")
        elif random_num == 6:
            print("윤현우 청소 당첨!")
        elif random_num == 7:
            print("유승균 청소 당첨!")
    time_duration = 10
    time.sleep(time_duration)
