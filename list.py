s = [1, 'four', 9, 16, 25] # 리스트를 만들고 값을 넣는 방법 
# 엘리먼트 

print(s)
print(s[0])
print(s[1]) # 들어간 리스트의 값을 꺼내는 방법 

print(len(s)) # 몇개의 값이 있는가를 알아내는가 

s[1] = 4 #s에 첫번째 값 four를 4라고 지정 
print(s)

#s.remove(9) #숫자 9를 찾아서 지움 
#s.append('nine')
#print(s)

del s[2] # 숫자를 0부터 순서대로 세서 2번째 자리 숫자를 지움 1 0번째 4 1번째 9 2번째
print(s)
s.append('hello') #리스트 추가 
print(s)

#스트링 리스트 는 시퀀스 
print("a"+"b")
print(["a"]+["b"])
print(len('hello'))
print(len(['a','b','c']))

print('hello'.capitalize()) #앞글자를 대문자로 바꿔줌 hello는 str라 capitalize가 가능
#print([1,2,3].capitalize()) # 1 2 3 리스트는 str이 아니라 capitalize 기능을 사용못함 
[1, 2, 3]
a = ['hello','world','python']
print(a[0])
person = {'name' : 'bae', 'age' : 17 , 'food' : 'hamburger'}
print(person['name']) # 대괄호
print(person['age'])
print(person['food'])