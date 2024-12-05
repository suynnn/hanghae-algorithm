'''
문제 1. 조명 ( #15736 )

총 N개의 초록색 조명이 있습니다.

이 조명은 버튼을 눌러서, 초록색 >  빨간색 > 초록색 으로 바꿀 수 있습니다.

1부터 N명까지의 학생들이 나와서 자신의 순서의 배수에 해당하는 조명에 버튼을 눌러서 색을 바꿉니다.

숫자 N이 주어졌을 때, N명의 학생들이 모두 버튼을 누른 뒤 남은 빨간색 조명의 개수를 출력하세요.

'''

n = int(input())
lighting = [False] * (n+1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        lighting[j] = not lighting[j]

answer = lighting.count(True)
print(answer)