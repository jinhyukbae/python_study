#print("Content-type: text/html") #웹서버에 아래 내용이 html이다 라고 선언  
#print()
import cgi, os
form = cgi.FieldStorage() # 서버에서 id 값을 불러올 때 사용 cgi라는 모듈을 쓰고 있기 때문에 위에 import cgi
title = form["title"].value #create.py title에 입력한 값이 적용 cgi라 썼으면 cgi
#create.py가 process_create.py에 전송하는 데이터는 78 79번째 줄에 title과 description
description = form['description'].value #create.py description에 입력한 값이 적용 cgi is라 입력 했으면 cgi is 

#print(title, description)
opened_file = open('data/'+title, 'w')#데이터 디렉토리 아래 타이틀이라는 파일을 write 전용으로 오픈 
opened_file.write(description) #디스크립션에 해당되는 값이 데이터 타이틀에 해당되는 파일에 쓰기가 된다.
# title을 cgi라 입력 description을 cgi is라 입력하고 submit을 한 결과 data 폴더에 cgi라는 제목과 cgi is라는 내용을 가진 파일이 생성 되었다.
opened_file.close()

#redirection 웹서버가 지정된 곳으로 보내버리는 헤더
print("Location: index.py?id="+title) #웹서버가 브라우저에게 이 주소로 이동해 Location
print()