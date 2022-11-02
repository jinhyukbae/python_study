'''
import math2     # 모듈 math2라는 파일에서 뭔가를 가져옴  math2모듈을 임포트 한 것 

print(math2.average(1,2,3))
print(math2.plus(1,2))  
print(math2.pi) 
'''

from math2 import average, plus, pi # 에버리지 플러스 파이라는 함수를 메스라는 모듈에서 임포트 한 것

print(average(1,2,3))
print(plus(1,2))  
print(pi)

#math2가 빠져도 구동이 된다.