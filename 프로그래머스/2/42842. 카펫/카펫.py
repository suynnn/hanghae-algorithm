def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow//2+2):
        if yellow % i == 0:
            if ((yellow//i+2)*2) + (i*2) == brown:
                answer.append(yellow//i+2)
                answer.append(i+2)
                break
    
    return answer