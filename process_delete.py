#print("Content-type: text/html") #웹서버에 아래 내용이 html이다 라고 선언  
#print()
import cgi, os
form = cgi.FieldStorage() # 서버에서 id 값을 불러올 때 사용 cgi라는 모듈을 쓰고 있기 때문에 위에 import cgi
pageId=form["pageId"].value

os.remove('data/'+pageId)

#redirection 웹서버가 지정된 곳으로 보내버리는 헤더
print("Location: index.py") #삭제가 끝나면 index.py로 보냄
print()

#만들었던 html5를 delete 하면 그 페이지가 삭제 되고 index.py로 오게된다.