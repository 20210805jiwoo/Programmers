# 방법 1
def solution(n, lost, reserve):
    u = [1] * (n + 2)
    for i in reserve:
        u[i] += 1
    for i in lost:
        u[i] -= 1
    for i in range(1, n+1):
        if u[i-1] == 0 and u[i]==2:
            u[i-1:i+1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]
    return len([x for x in u[1:-1] if x >0])

# 방법 2
def solution(n, lost, reserve):
    s = set(lost) & set(reserve) # 가져왔는데 잃어버린
    l = set(lost) - s # 잃어버린 애 중 체육복 없는 학생 집합
    r = set(reserve) - s # 체육복 있는 학생 중 도난 X 학생

    # 앞뒤로 체육복 없는 학생에게 빌려줌
    for x in sorted(r):
        if x - l in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
