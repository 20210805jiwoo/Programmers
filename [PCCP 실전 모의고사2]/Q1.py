def solution(input_string):
    answer = ''
    
    str_list = [input_string[0]]
    for i in input_string:
        if i != str_list[-1]:       # 한 문자가 연속적으로 나타난 경우 제거
            str_list.append(i)
    
    ans = set(str_list)
    ans = sorted(ans)       # ans 딕셔너리를 알파벳 순으로 정렬함
        
    for i in ans:
        cnt = 0
        for j in str_list:
            if i == j:
                cnt += 1
        if cnt > 1:
            answer += i
    
    if answer == '':
        answer += 'N'
    
    return answer
