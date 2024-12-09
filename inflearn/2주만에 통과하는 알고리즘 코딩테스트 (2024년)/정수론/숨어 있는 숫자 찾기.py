'''
문제 3. 숨어 있는 숫자 찾기 ( #1407, # 2247 )


숨어있는 숫자의 범위 A,B가 주어진다.

A에서 B까지 숫자를 나열해서,

각각의 숫자에서 2의 제곱수로 나누어지는 약수를 찾아 모두 더해서 출력하시오.

'''

a, b = map(int, input().split())

answer = 0
for i in range(a, b+1):

    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            if j % 2 == 0:
                answer += j

print(answer)

