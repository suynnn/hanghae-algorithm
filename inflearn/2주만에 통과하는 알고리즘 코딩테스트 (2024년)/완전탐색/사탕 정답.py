'''
문제 2. 사탕  ( # 14568 )
친구 A,B,C에게 사탕을 나누어 주려고 합니다.
조건은 아래와 같습니다.
1.     남는 사탕이 없어야 합니다.
2.     A는 B보다 2개 이상 많은 사탕을 가져야 합니다.
3.     셋 중 사탕을 하나도 못 받는 친구는 없어야 합니다.
4.     C가 받는 사탕의 수는 짝수입니다.
분배 가능한 경우의 수를 출력하는 프로그램을 작성해주세요

'''

candy = int(input())

answer = 0
for a in range(0, candy+1):
    for b in range(0, candy + 1):
        for c in range(0, candy + 1):
            if a + b + c == candy:
                if a >= b + 2:
                    if a != 0 and b != 0 and c != 0:
                        if c % 2 == 0:
                            answer += 1

print(answer)