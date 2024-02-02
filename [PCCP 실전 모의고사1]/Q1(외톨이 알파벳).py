# 방법 1
def solution(input_string):
    answer = ''

    str_list = [input_string[0]] # 리스트 생성, 첫 번째 문자 리스트에 추가
    for i in input_string: # 문자열 순회하면서
        if i != str_list[-1]: # 한 문자가 연속적으로 나타난 경우 제거
            str_list.append(i)
    
    ans = set(str_list) # 중복 제거 위해 set 자료형으로 변환
    ans = sorted(ans) # 알파벳 순으로 정렬

    for i in ans:
        cnt = 0
        for j in str_list:
            if i==j:
                cnt += 1
        if cnt > 1:
            answer += i
    if answer == '':
        answer += 'N'

    return answer

# 방법 2 
import collections
def solution(input_string):
    answer = ''
    sH = collections.defaultdict(int) # 빈 딕셔너리 생성(문자와 등장 횟수 기록)
    prev = None
    for cur in input_string:
        if cur != prev: # 현재 문자가 직전 문자와 같은지 확인
            sH[cur] += 1 # 다를 경우에만 딕셔너리에 추가, 해당 문자 횟수 1로 초기화
        prev = cur
    for [key, val] in sH.items(): # 등장 횟수 2 이상인 문자들 answer에 추가
        if val >= 2:
            answer += key
    if len(answer) == 0: # 비어있다면
        return "N"
    
    return ''.join(sorted(answer))
