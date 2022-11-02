import os
def getList(): 
  files = os.listdir('data')  #import os를 안해주면 os가 에러 뜸
  listStr = ''
  for item in files:
      listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
  return listStr
