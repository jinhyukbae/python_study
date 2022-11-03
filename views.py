from django.shortcuts import render , HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt


nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'routing is ..'},
    {'id':2, 'title':'view', 'body':'view is ..'},
    {'id':3, 'title':'model', 'body':'model is ..'},
]

#html코드를 함수화

def HTMLTemplate(articleTag):
    global topics
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
            <a href="/create/">create</a>
        </ul>
    </body>
    </html>
    '''


 
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
    return HttpResponse(HTMLTemplate(article)) 

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