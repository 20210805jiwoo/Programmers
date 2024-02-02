def solution(number, k):
    collected = [] # 빈 리스트 생성(결과 담을 임시 저장소)
    for i, num in enumerate(number):
        # 리스트 비어있지 않고, 마지막으로 추가된 숫자가 현재 숫자보다 작고, 제거해야 할 숫자 남아있을 때까지 반복
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop() # 마지막 숫자 제거
            k -= 1
        if k == 0: # 이미 필요한 숫자 다 수집한 상태
            collected += list(number[i:]) # 남은 숫자들 collected 리스트에 추가
            break
        collected.append(num) 

    collected = collected[:-k] if k > 0 else collected # k 아직 남아있으면 결과에서 뒤에서 k 만큼의 숫자 제외
    answer = ''.join(collected) # collected 리스트에 있는 숫자들 문자열로 합쳐 반환
    return answer
