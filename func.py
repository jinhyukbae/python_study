'''
#code...
a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)
#code....

'''

#파이썬은 함수 시작할 때 def를 써야함

'''
def average(): 

    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3


average()
'''


'''
# 함수의 인풋 
#매개변수 파라미터 a b c
#인자 아규먼트 10 20 30 아규먼트 10을 입력한 것이고 그 것을 파라미터 a가 받아서 내부에서 사용중 
def average(a,b,c): 

    s=a+b+c
    r=s/3
    print(r)


average(10,20,30) # 10 20 30에 대한 평균값을 구해줌 a=10 b=20 c=30 하고 s=a+b+c하면 60 r=60/3 = 20

'''

def average(a,b,c): 

    s=a+b+c
    r=s/3
    return r


print(average(10,20,30))

def a():
    return 'haha'
print(a())

# a라는 함수를 호출하면 a라는 함수는 return 뒤에나오는 값이 된다 

