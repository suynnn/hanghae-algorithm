'''
[문제 분석]
- 팀 이름 규칙
    1. 세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열
    2. 세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열
- 백준 온라인 저지에서 해결한 문제의 개수, 입학 연도, 그리고 성씨가 주어지면 첫 번째 방법과 두 번째 방법으로 만들어지는 팀명을 차례대로 출력

[의사결정]
- 첫 번째 방법으로 팀명 짓기 - 입력된 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬
- 두 번째 방법으로 팀명 짓기 - 문제푼 수와 이름을 2차원 배열에 담아서 문제 푼 수를 기준으로 내림차순 정렬. 그리고 정렬된 리스트에서 각 이름 첫글자 데이터 가져와서 팀명 짓기

'''

years = []
members = []

# 입력받고 입학연도, 문제 푼 수 및 이름 데이터 각각 리스트에 삽입
# members는 2차원 리스트로 사용
for _ in range(3):
    p, y, s = input().split()

    years.append(int(y))
    members.append([int(p), s])

# 입학연도 오름차순으로 정렬
years.sort()

team_name1 = ''
for x in years:
    team_name1 += str(x % 100)

print(team_name1)

# 2차원 리스트 members에서 문제 푼 수를 기준으로 내림차순 정렬
members.sort(key=lambda x:x[0], reverse=True)

# 이름 첫 글자만 가져와서 팀명 짓기
team_name2 = ''
for x in members:
    team_name2 += x[1][0]

print(team_name2)