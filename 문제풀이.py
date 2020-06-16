# 해쉬 문제

# 1번

import pandas as pd
pd.DataFrame
type(pd.DataFrame(['a','b'])[0])
pd.Series(['a','b']).isin(['a'])
[0,1]
def solution(participant, completion):
    import pandas as pd
    x=pd.Series(participant).isin(completion)
    for i in range(len(x)):
        y=x[i]
        if y!=True:
            answer=participant[i]
    return answer
solution(['leo', 'kiki', 'eden'],['eden', 'kiki'])
participant=['leo', 'kiki', 'eden']
completion=['eden', 'kiki']
def solution(participant,completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if i == (len(participant) - 1):
            answer = participant[i]
            break
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    if answer == '':
        answer = participant[len(participant) - 1]

    return answer

def solution(participant, complete) :
    participant.sort()
    complete.sort()

    for part, comp in zip(participant, complete) :
        if part != comp :
            return part
    return participant[-1]

# 2번

def solution(phone_book):
    answer=False
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
            answer=phone_book[i+1].startswith(phone_book[i])
            if answer:
                break
        elif len(phone_book[i]) > len(phone_book[i+1]):
            answer = phone_book[i].startswith(phone_book[i+1])
            if answer :
                break
    if answer==True:
        answer=False
    elif answer==False:
        answer=True
    return answer

# 124 나라
n=10
x={1:1,2:2,4:3}
x
x.keys()
x.values()

import numpy as np
n=13
x=int(np.log((2*n+1)/3)/np.log(3))+1
13/(x)

int('42')
def solution(n):
    x=int(np.log((2 * n + 1) / 3) / np.log(3))+1
    answer=''
    return int(answer)

solution(10)

# 모의고사

## 내 정답
def solution(answers):
    import numpy as np
    supo=[]
    supo.append(([1,2,3,4,5]*((len(answers)//5)+1))[:len(answers)])
    supo.append(([2 if i%2==0 else [1,3,4,5][(i-1)//2] for i in range(8)]*((len(answers)//8)+1))[:len(answers)])
    supo.append((list(np.repeat(np.array([3,1,2,4,5]),[2]))*((len(answers)//10)+1))[:len(answers)])
    result=[]
    for i in supo:
        result.append(sum([i[j]==answers[j] for j in range(len(answers))]))
    x=max(result)
    answer = [i+1 for i,j in enumerate(result) if j==x]
    return answer

## 다른사람 풀이
def solution(answers):
    pattern1=[1,2,3,4,5]
    pattern2=[2,1,2,3,2,4,2,5]
    pattern3=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    for idx,values in enumerate(answers):
        if values==pattern1[idx%len(pattern1)]:
            score[0]+=1
        if values==pattern2[idx%len(pattern2)]:
            score[1]+=1
        if values==pattern3[idx%len(pattern3)]:
            score[2]+=1
    x=max(score)
    answers=[i+1 for i,j in enumerate(score) if j==x]
    return answers
#### + cycle을 쓰면 리스트 무한반복 함