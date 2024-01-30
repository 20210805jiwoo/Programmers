def solution(numbers):
    # 각 숫자를 문자열로 변환
    numbers = [str(x) for x in numbers]

    # 정렬 기준을 설정하여 내림차순으로 정렬
    # - key=lambda x: (x * 4)[:4]: 각 숫자를 4번 반복하여 길이를 맞추고, 앞 4자리까지 비교
    # - reverse=True: 내림차순 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)

    # 정렬된 숫자를 이어붙여 가장 큰 수 생성
    if numbers[0] == '0':
        answer = '0'  # 가장 큰 수가 0으로 시작할 경우, '0' 반환
    else:
        answer = ''.join(numbers)
    return answer
