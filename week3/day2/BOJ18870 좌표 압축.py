'''
[문제 분석]
- 주어진 좌표 값들을 작은 값부터 차례대로 0부터 n-1까지의 값으로 압축해서 출력
- 각 좌표가 얼마나 작은지에 따라 압축된 값으로 변환

[의사결정]
- 중복을 제거하고 좌표를 정렬해서 좌표의 순서를 확정시킴
- 좌표 값을 키로, 좌표의 압축된 값을 값으로 저장해서 빠르게 압축된 좌표 값을 찾을 수 있게 했음
'''

n = int(input())
x_list = list(map(int, input().split()))

# 중복된 좌표를 제거하고 오름차순으로 정렬
sorted_list = sorted(set(x_list))

# 각 좌표를 압축된 값으로 저장할 딕셔너리 선언
coordinate = {}

# 좌표 리스트를 반복문으로 좌표의 압축 값을 0부터 차례대로 부여
for idx, value in enumerate(sorted_list):
    coordinate[value] = idx

# 원래 좌표 리스트에서 각 좌표의 압축 값 출력
for x in x_list:
    print(coordinate[x], end=' ')