from sys import stdin
from collections import deque

n = int(input())

students = deque()
max_student_cnt = 0
student_num = 0

for _ in range(n):
    info = list(map(int, stdin.readline().rstrip().split()))

    if info[0] == 1:
        students.append(info[1])

        if max_student_cnt < len(students):
            max_student_cnt = len(students)
            student_num = students[-1]
        elif max_student_cnt == len(students):
            if student_num > students[-1]:
                student_num = students[-1]

    elif info[0] == 2:
        students.popleft()

print(f'{max_student_cnt}' + ' ' + f'{student_num}')