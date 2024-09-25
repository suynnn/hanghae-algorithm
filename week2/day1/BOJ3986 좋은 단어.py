# 각각 단어 길이만큼 for문을 돌려서 스택에 쌓는다
# 스택 맨 위에 같은 글자가 들어있다면 pop() 해주는 식
# 단어 길이 끝까지 실행시켰을 때 스택에 아무 글자도 남아있지 않다면 좋은 단어 인것

from sys import stdin

n = int(stdin.readline())
cnt = 0

for _ in range(n):
    # strip() : 문자열 양 옆의 \n 혹은 \t를 제거
    word = stdin.readline().strip()

    stack = []
    for x in word:
        # 스택이 비어있거나 맨 위의 글자랑 일치하지 않을 때 스택에 추가
        if not stack or stack[len(stack)-1] != x:
            stack.append(x)
        else:
            stack.pop()

    # 스택이 비어있다면 좋은 단어인 것이므로 카운트해줌
    if not stack:
        cnt += 1

print(cnt)