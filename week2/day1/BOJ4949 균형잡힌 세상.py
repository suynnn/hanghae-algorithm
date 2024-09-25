# 의사결정
# - 각 문장을 문장길이 만큼 for문을 돌려서
#     - ( 괄호를 만나면 스택에 넣고 ) 괄호 차례 일때는 스택의 맨 위에 있는 괄호가 ( 이라면 pop() 해준다
#     - [ 괄호도 마찬가지로 똑같은 매커니즘을 가진다

from sys import stdin

while True:
    # 문장 맨 뒤의 \n 제거
    strs = stdin.readline()[:-1]

    if strs == '.':
        break

    # 괄호들을 저장할 stack 리스트와 괄호가 맞게 짝지어졌는지 확인하는 isBalanced 선언
    stack = []
    isBalanced = True

    for x in strs:
        if x == '(' or x == '[':
            stack.append(x)

        elif x == ')':
            # 스택이 비어있거나 맨 위의 값이 (가 아니라면 짝 지을 수 없는 것이므로 isBalanced를 False로 바꾸고 바로 반복문 끝냄
            if not stack or stack[-1] != '(':
                isBalanced = False
                break
            stack.pop()

        elif x == ']':
            # 스택이 비어있거나 맨 위의 값이 [가 아니라면 짝 지을 수 없는 것이므로 isBalanced를 False로 바꾸고 바로 반복문 끝냄
            if not stack or stack[-1] != '[':
                isBalanced = False
                break
            stack.pop()

    # isBalanced가 True고 stack이 비어있어야 괄호들이 잘 짝지어진 것
    if isBalanced and not stack:
        print('yes')
    else:
        print('no')