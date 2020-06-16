# 파이썬을 파이썬 답게

# divmod
## 작은 숫자를 다룰때는 //(몫) 또는 %(나머지) 가 더 좋을 수 도 있지만 큰 숫자의 경우 divmod 활용이 더 빠르다
a,b=5,4
print(a//b,a%b)
print(*divmod(a,b))

# n 진법으로 표기된 string을 10진법으로 표시하기

## 나의 풀이법
num, base = map(int, input().strip().split(' '))
sum=0
for i,j in enumerate(list(str(num))[::-1]):
    sum+=int(j)*(base**i)
print(sum)

## python 정석 풀이법
### 파이썬의 int(x, base = 10) 함수는 진법 변환을 지원함
int('21',5)
num,base=map(int,input().strip().split(' '))
sum=int(str(num),base)
print(sum)

# tip : input 받을때 strip으로 혹시 모를 앞이나 마지막의 띄어쓰기 또는 \n 등을 없애주기 ex) a,b = map(int,input().strip().split(' '))
# tip : list 나 튜플 print로 반환할때 * 앞에 쓰면 [],() 없어짐!