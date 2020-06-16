def solution(d, budget):
    d_1=sorted(d)
    for i,j in enumerate(d_1):
        budget=budget-j
        if budget==0:
            break
        elif budget<0:
            i=i-1
            break
    answer = i+1
    return answer

solution([1,3,2,5,4],9)
sorted([1,4,2,3])


def solution(s):
    s_1=s.split(" ")
    p=[]
    for k in s_1:
        k_1=list(k)
        x=[]
        for i,j in enumerate(k_1):
            if i%2==0:
                x.append(j.upper())
            else:
                x.append(j.lower())
        p.append("".join(x))
    answer = " ".join(p)
    return answer

