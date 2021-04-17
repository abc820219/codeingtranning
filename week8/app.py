import mysql.connector
import json
import secrets
import time
from flask import Flask,request,redirect,render_template,session,make_response
from datetime import timedelta
# 連線
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="website"
)

mycursor = mydb.cursor()
# 執行sql語法
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")

# 靜態資料夾
app = Flask(
    __name__,
    static_folder = "templates", #靜態資料夾
    static_url_path = "/" #對應的網址路徑
    ) # create app
# session密碼
app.secret_key = "hello"
# seesion持續時間
app.permanent_session_lifetime =  timedelta(minutes=5)

cookieStatus = {}

# 路由
# 首頁
@app.route("/")
def index():
  cookieValue = request.cookies.get("sessionid")
  if cookieValue in cookieStatus:
    return redirect('/member')
  return render_template('/index.html')

# 註冊頁
@app.route('/signup')
def registerHandler():
  return render_template('/signup.html')

# 會員頁面
@app.route("/member")
def memberHandler():
  cookieValue = request.cookies.get("sessionid")
  # 是否存在cookie並且沒有過期
  if cookieValue in cookieStatus and time.time() < cookieStatus[cookieValue]["expires_time"]:
    return render_template('/member.html',name=cookieStatus[cookieValue]['name'])
  else:
    return redirect("/")

# 查詢會員
@app.route("/api/users")
def getusersHandler():
  username = request.args.get('username')
  sql = f"SELECT * FROM user WHERE username like '{username}'"
  mycursor.execute(sql)
  result = mycursor.fetchone()
  if result != None:
    data = {
      'data':{
      'id':result[0],
      'name':result[1],
      'username':result[2]
      }
    }
    json_str = json.dumps(data, indent=3)
    return json_str
  else:
    data = {
    'data': None
    }
    json_str = json.dumps(data, indent=3)
    return json_str

# 修改
@app.route("/api/user",methods=["POST"])
def edituserHandler():
  req = request.get_json()
  cookieValue = request.cookies.get("sessionid")
  # 錯誤判斷
  try:
    username = req['username']
    sql = f"update user set username = '{username}' where id ='{cookieStatus[cookieValue]['id']}'"
    mycursor.execute(sql)
    mydb.commit()
    sql = f"SELECT * FROM user WHERE id like '{cookieStatus[cookieValue]['id']}'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    data = {
        'data':{
        'id':result[0],
        'name':result[1],
        'username':result[2],
        "ok":True
        }
    }
    session["name"] = username
    json_str = json.dumps(data, indent=3)
    return json_str
  except:
    data = {
      "error":False
    }
    json_str = json.dumps(data, indent=3)
    return json_str    


# 失敗頁面
@app.route('/error')
def errorHandler():
  # 取得url query
  message = request.args.get('message','預設錯誤')
  return render_template('/error.html',message=message)

# 註冊api
@app.route('/sign',methods=["POST"])
def signHandler():
  name =  request.form["name"]
  username = request.form["username"]
  password = request.form["password"]
  sql = f"SELECT count('id') FROM user WHERE username like '{username}'"
  mycursor.execute(sql)
  flag = False
  for x in mycursor:
    if x[0] != 0:
       flag = True
    if flag == True:
      return redirect("/error?message=帳號已被註冊")
    else:
      # sql語法
      sql = f"insert into user values(null,'{name}','{username}','{password}',now())"
      # 執行
      mycursor.execute(sql)
      # 刪除 新增 修改 要多一個commit
      mydb.commit()
      return redirect("/")

# 登入api
@app.route("/signin",methods=["POST"])
def loginHandler():
  # REST API用
  # print(request.get_json())
  # return json.dumps({'name':'a','words':'b'})
  name =  request.form["name"]
  username = request.form["username"]
  password = request.form["password"]
  id = None
  # sql字串
  sql = f"SELECT count('id'), id FROM user WHERE username like '{username}' and name like '{name}' and password like'{password}'"
  # 執行sql
  mycursor.execute(sql)
  flag = False
  for x in mycursor:
    if x[0] != 0:
       id = x[1]
       flag = True
  if flag == True:
    secretKey = secrets.token_hex(16)
    expiresT = time.time() + 20 * 60
    cookieStatus[secretKey] = {}
    cookieStatus[secretKey]["name"] = name
    cookieStatus[secretKey]["id"] = x[1]
    cookieStatus[secretKey]["expires_time"] = expiresT
    resp = make_response(redirect('/member'))
    resp.set_cookie(key="sessionid",value=secretKey,expires=expiresT,httponly=True,samesite="Strict")
    return  resp
  else:
    return redirect("/error?message=登入錯誤")

# 登出api
@app.route("/signout")
def logoutHandler():
  # 刪除cookie
  cookieValue = request.cookies.get("sessionid")
  cookieStatus.pop(cookieValue)
  outResp = make_response(redirect('/'))
  outResp.set_cookie(key="sessionid",value="",expires=0)
  return outResp

# server啟動
app.run(port=3000)


#參考資源
# sql語法
# https://www.w3schools.com/python/python_mysql_getstarted.asp
# 實作資源
# https://www.796t.com/article.php?id=182314
# REST API
# https://medium.com/%E4%B8%80%E5%80%8B%E4%BA%BA%E7%9A%84%E6%96%87%E8%97%9D%E5%BE%A9%E8%88%88/python-flask-rest-api%E7%AD%86%E8%A8%98-869c3d2fee3
# 基本操作
# 澎澎udemy
# crud python & mysql
# https://www.youtube.com/watch?v=91iNR0eG8kE&list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-&index=2
# 錯誤判斷
# https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-edd15e2b5d1e
# session操作
# https://blog.csdn.net/qq_42817166/article/details/83512544
# fetch
# https://blog.csdn.net/u014234260/article/details/79581041

# v2 cookie
