print("Content-type: text/html")
print()
import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    # files=item으로 인식 files=os.listdir('data')로 데이터 폴더에 있는 리스트로 files=item=list가 됨
    # listStr 을 ''로 지정하고 공백 + files를 리스트를 false 값이 나올 때 까지 반복 ex) css html javascript python 출력 후 그 뒤는 공백=false이므로 중단 
#print(listStr)


#데이터폴더리스트=files=item=name
#


from pydoc import describe
form = cgi.FieldStorage()
# html은 index.py에 갇혀있고 실제 데이터는 data폴더에 파일로 깔끔하게 저장 됨  
# form 안에 id 값이 있으면 true 없으면 false 
# http://127.0.0.1/index.py?id=html 은 뒤에 id 값이 세팅 되어 있으므로 세팅된 값이 나옴 id=html
# http://127.0.0.1/index.py 는 뒤에 id 값이 없으므로 else 값 hihihi가 나옴 
if 'id' in form: 
    pageId = form["id"].value
    description = open('data/'+pageId, 'r',encoding='UTF-8').read()
    #html을 클릭했다면 id는 html이고 pageid의 값은 html이 된다. '폴더'/+pageId하면 폴더html이 된다.
    #파일을 열고 읽기모드로 연 파일에 대해서 읽는다 read 그 결과를 description 이라는 변수에 담겠다 
    # description = open('data/'+pageId, 'r').read() 만 해서 안되면 ,encoding='UTF-8'
else:
    pageId = 'hihihi'
    # id 값이 없을 때 디스크립션이라는 변수의 값이 hello hello가 된다.
    description = 'Hello hello'

    #<meta charset="UTF-8">써서 한글이 깨지면 <meta charset="euc-kr"> 
print('''<!doctype html>
<html>
<head>
<title>WEB1 - html</title>

<meta charset="euc-kr">


<link rel="stylesheet" href="style.css">

<script src="color.js"></script>

</head>

<body>

  


  <h1><a href="index.py?id=WEB">WEB</a></h1>





  
<ol>
 {listStr}
</ol>




<a href="create.py">create</a>

<!--form은 url 쿼리스트링을 만드는 기능 url 
process_create.py?title=CGI&description=CGI+IS.. 
form action으로 process_create.py로 전송 됐고
타이틀에 CGI라 쓰고 description에 cgi is라고 적고 서브밋을 눌렀으므로
title=cgi&description=cgi+is로 출력이 된다. 이러한 역할을 하는 게 url 쿼리스트링 
process_create.py로 아래 정보를 전송한다는 뜻 method=""은 method="get"과 같다
method="post"로 하면 url 변경 x 크롬 검사창(f12) 네트워크에 은밀하게 전송 -->


<!--<form action="process_create.py" method="post"> 변경전-->

    <form action="process_update.py" method="post">
    <input type="hidden" name="pageId" value="{form_default_title}">
    <!--서브밋을 눌렀을 때 히든으로 하게 되면 pageid라 하는 값으로 데이터가 전송될 때 {form_default_title}에 해당하는 정보가 은밀하게 전송됨  -->

    <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p> 
    <!-- 네임의 타이틀은 서버에 전송될때 글상자에 입력한 정보를 타이틀이라는 이름으로 전송하겠다  -->
    <!-- 인풋 태그에  기본값을 넣고 싶을 땐 value 타이틀에 hi가 기본적으로 뜨게 됨   -->

    <p><textarea rows="4" name="description" placeholder="description" value="{form_default_description}"></textarea></p> 
    <!--텍스트상자 에 입력한 정보는 description이라는 이름으로 전송된다 -->
    
    <p><input type="submit"></p> <!--제출버튼 -->
</form>

</div>
</div>








</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description))

# format에 desc=description을 추가하고 <p></p> 자리에 {desc}를 추가하면 저 자리에 id값이 없을 때 description = 'Hello hello'이 실행된다.

