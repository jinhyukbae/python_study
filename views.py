from django.shortcuts import render , HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'routing is ..'},
    {'id':2, 'title':'view', 'body':'view is ..'},
    {'id':3, 'title':'model', 'body':'model is ..'},
]

#html코드를 함수화

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        #홈에서는 삭제 버튼이 없고 다른 페이지로 가면 삭제버튼이 있게 id가 있을 때 (none)이 아닐 때 ture 가 되는 != 사용 
        contextUI = f'''
        <li>
            <form action="/delete/" method="post">
                <input type="hidden" name="id" value={id}> 
                <input type="submit" value="delete">
            </form>
        </li>
        <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:    
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
    <h1><a href="/">Django</a></h1>
    <ul>
        {ol}
    </ul>
    {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''
# <form action="/delete/" /delete/라는 페이지로 감 method="post"> 은밀한 방식으로

 
def index(request):
    article = '''
    <h2>welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))
    
    
def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'            
    return HttpResponse(HTMLTemplate(article, id)) 

#삭제하려는 글의 번호를 전달하게 하려면 read 페이지에 HTMLTemplate으로 들어올 때 두번 째 인자로 id값을 전해주고 위에 def HTMLTemplate에 id값을 받는 파라미터 인자를 써줌

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title" :title, "body":body}
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        topics.append(newTopic)
        return redirect(url)


@csrf_exempt
#GET 방식으로 들어왔을 때랑 POST 방식으로 들어왔을 때를 구별할 필요가 있음 
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {"title":topic['title'], "body":topic['body']}
        article = f'''
        <form action="/update/{id}/" method="post">
            <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
            <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST': #서버 쪽의 전송된 데이터를 가지고 토픽스 변수의 값을 바꾸는 식 아래 
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics: #토픽스에서 일치하는 값 for문 으로 뽑기 
            if topic['id'] == int(id): #일치한다면 값을 변경시켜줌 
                topic['title'] == title
                topic['body'] == body
        return redirect(f'/read/{id}') # 과정에 성공했다면 사용자를 /read/{id}로 보냄 



@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id): #양쪽이 같지 않다면 != 쓰면 서로 다를 때 true
                newTopics.append(topic) # topic id와 int id가 다를 때 newtopics를 추가 append
        topics = newTopics # 
        return redirect('/') #위 과정이 끝나면 '/' (홈)으로 사용자를 보냄        



# 클라이언트로 정보를 전송하기 위한 함수 def index 첫번째 파라미터의 인자로 request 보편적으로 씀
# 처리한 결과를 클라이언트로 보낼 때 return값 http를 이용해서 응답을 하겠다는 의미에서 httpresponse
# 전송하고 싶은 값을 괄호에 넣는다
# 

##ol 코드임 
#def index(request):
    #global topics
    #ol = ''
    #for topic in topics:     # topic을 순서대로 하나하나씩 꺼냄 앞에다 f 붙이면 중괄호 사용 가능
        #ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>' # topic에 title 값을 하나하나씩 리스트 적용하여 화면에 띄움 
        #링크 "/read/{topic["id"] 걸면 routing을 누르면 read1 view를 누르면 read2 model을 누르면 read3으로 감
    #topics = global topics 전역 변수
    #return HttpResponse(HTMLTemplate())
    #return HttpResponse('<h1>Random</h1>'+str(random.random()))
    #접속을 할 때 마다 랜덤으로 숫자를 띄움