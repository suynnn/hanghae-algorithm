'''
문제 3. 연립방정식 ( # 19532 )
숫자 A,B,C,D,E,F 가 주어집니다.

다음 연립방정식에서 x와 y값을 계산하는 프로그램을 작성하세요.



범위
-	X와 Y는 -10000이상 10000이하인 정수이다.

'''

nums = list(map(int, input().split()))

for x in range(-10000, 10001):
    for y in range(-10000, 10001):
        if nums[0] * x + nums[1] * y == nums[2] and nums[3] * x + nums[4] * y == nums[5]:
            print(x, y)
            break
