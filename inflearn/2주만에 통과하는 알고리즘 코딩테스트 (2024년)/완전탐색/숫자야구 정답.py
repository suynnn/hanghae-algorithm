'''
문제 4. 숫자야구 ( # 2503 )

A는 3자리 숫자로 된 정답을 하나 정합니다.

B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 합니다.

B가 말한 숫자가 정답에 포함되어 있다면 1 Ball입니다.
B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike입니다.

다른 숫자로 이루어진 세 자리수

Strike와 Ball의 결과를 보고, 가능한 숫자를 계산하는 프로그램을 작성하세요

'''

# a가 정답으로 생각할 수 있는 모든 수 넣어보기
# 그리고 a가 도전한 내용에 맞는지 확인하기

n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]

answer = 0
for a in range(1, 10): # 100의 자리 수
    for b in range(1, 10): # 10의 자리 수
        for c in range(1, 10): # 1의 자리 수

            if (a == b or b == c or a == c):
                continue

            cnt = 0

            # 숫자가 정해졌다면
            for arr in hint:
                number = arr[0]
                expected_strike = arr[1]
                expected_ball = arr[2]

                ball_count = 0
                strike_count = 0

                # 정답 숫자 분리
                num_a = number // 100
                num_b = (number // 10) % 10
                num_c = number % 10

                strike_count = 0
                ball_count = 0

                # Strike 계산 (같은 자리, 같은 숫자)
                if a == num_a:
                    strike_count += 1
                if b == num_b:
                    strike_count += 1
                if c == num_c:
                    strike_count += 1

                # Ball 계산 (다른 자리, 같은 숫자)
                if a == num_b or a == num_c:
                    ball_count += 1
                if b == num_a or b == num_c:
                    ball_count += 1
                if c == num_a or c == num_b:
                    ball_count += 1

                # 힌트와 일치하는지 확인
                if strike_count == expected_strike and ball_count == expected_ball:
                    cnt += 1

            if cnt == n:
                answer += 1

print(answer)