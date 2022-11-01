print("Content-type: text/html")
print()
import cgi, os

files = os.listdir('data') #listdir 함수의 입력값으로 data라고하는 str 주면 listdir라는 함수는 data라는 파일 목록을 리스트에 담아서 반환해주는 함수 
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
    description = open('data/'+pageId, 'r', encoding='UTF-8').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId) #format에 의해서 중괄호 부분이 pageId값으로 대체 
    delete_action = '''
    <form action="process_delete.py" method="post"> 
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
    </form>

    '''.format(pageId) #클릭했을때 process_delete 페이지로 이동 뭘지울건지 name=pageId
    
    #업데이트 버튼은 페이지로 이동 삭제는 클릭했을 때 삭제가 바로 일어나서 링크로 처리하는 게 아니라 폼으로 처리 링크로 처리하면 그 링크를 클릭하는 순간 삭제가 일어날 수도 있으므로

    #html을 클릭했다면 id는 html이고 pageid의 값은 html이 된다. '폴더'/+pageId하면 폴더html이 된다.
    #파일을 열고 읽기모드로 연 파일에 대해서 읽는다 read 그 결과를 description 이라는 변수에 담겠다 
    # description = open('data/'+pageId, 'r').read() 만 해서 안되면 ,encoding='UTF-8'
else:
    pageId = 'hihihi'
    # id 값이 없을 때 디스크립션이라는 변수의 값이 hello hello가 된다.
    description = 'Hello hello'
    update_link = '' # id값이 없다면 업데이트할 대상이 없기때문에 공백으로 둠 
    delete_action = ''
    #<meta charset="UTF-8">써서 한글이 깨지면 <meta charset="euc-kr"> 
print('''<!doctype html>
<html>
<head>
<title>WEB1 - html</title>

<meta charset="euc-kr">


<link rel="stylesheet" href="style.css">

<script src="color.js"></script>

</head>
<a href=""></a>
<body>

  


  <h1><a href="index.py?id=WEB">WEB</a></h1>


<!--  -->


  <div id="grid">
<ol>
 {listStr}
</ol>


<div id="article">

<a href="create.py">create</a>
{update_link}
<!-- <a href="update.py">update</a> 이 부분이 {update_link}가 됨-->
{delete_action}
<h2>{title}</h2>
<p>{desc}</p>


</div>
</div>








</body>
</html>'''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))

# format에 desc=description을 추가하고 <p></p> 자리에 {desc}를 추가하면 저 자리에 id값이 없을 때 description = 'Hello hello'이 실행된다.

