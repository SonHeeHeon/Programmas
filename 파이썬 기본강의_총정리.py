# Random 패키지
import random
list = ["빨","주","노","초","파","남","보"]
# 여기에 코드를 작성해 보세요.
random.shuffle(list)
list

# 딕셔너리 지우기
def check_and_clear(box):
    if "불량품" in box.keys():
        del(box['불량품'])
    else:
        pass
box1 = {"불량품" : 10}
check_and_clear(box1)
print(box1)
box2 = {"정상품": 10}
check_and_clear(box2)
print(box2)
# Enumerate() => 리스트에 인덱스를 주어 튜플로 반환
list_1=[1,2,4,8,16]
for i in enumerate(list_1):
    print(*i) # *를 하면 둘이 한꺼번에 출력됨
for i in enumerate(list_1):
    print(i[0],i[1])
for i,j in enumerate(list_1):
    print(i,j)

#★★★★★★★★★★★★★★★★★★ 중요!!!!!!!!!!!!!
## Pass 와 Continue 는 다름!!
## Pass는 바로 다음 루프로 넘어가지 않고 그뒤의 것을 수행함 Continue는 바로 다음 루프로 넘어간다
for i in range(3):
    if True:
        print('pass',i)
        pass
    print('son')
for j in range(3):
    if True:
        print('pass',j)
        continue
    print('son')

# Try , Except => if,else로 해결되는경우도 있음
text_1='100%'
try:
    number_1=int(text_1)
except ValueError:                          # error명이 뭔지 오류가 뜨는걸 실행시켜 보면 나옴
    print('{}은 숫자가 아니네요',text_1)

def safe_index_out(list,index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{}번째 인덱스 값이 리스트에 없습니다'.format(index))
safe_index_out([1,2,3],4)
def safe_index_out(list,index):
    if len(list)>index:
        print(list.pop(index))
    else:
        print('{}번째 인덱스 값이 리스트에 없습니다'.format(index))
safe_index_out([1,2,3],2)

try:
    list_1=[]
    print(list_1[0])
    text_1='abc'
    print(int(text_1))
except:
    print('에러가 발생하였습니다')             ## 여러 종류의 에러가 함께 잇을때는 except 뒤에 에러명을 달지 않으면 처리됨


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