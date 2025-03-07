def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]

    answer = sorted(numbers, key=lambda x:x*3, reverse=True)
    
    res = ''.join(answer)
    if '0'*len(numbers) == res:
        return '0'
    else:
        return res