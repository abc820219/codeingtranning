import mysql.connector
import json
from flask import Flask,request,redirect,render_template,session
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

# 路由
# 首頁
@app.route("/")
def index():
  print(session)
  if "name" in session:
    return redirect('/member')
  return render_template('/index.html')

# 註冊頁
@app.route('/signup')
def registerHandler():
  return render_template('/signup.html')


# 會員頁面
@app.route("/member")
def memberHandler():
  return render_template('/member.html',name=session["name"])

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
@app.route("/login",methods=["POST"])
def loginHandler():
  # REST API用
  # print(request.get_json())
  # return json.dumps({'name':'a','words':'b'})
  name =  request.form["name"]
  username = request.form["username"]
  password = request.form["password"]
  # sql字串
  sql = f"SELECT count('id') FROM user WHERE username like '{username}' and name like '{name}' and password like'{password}'"
  # 執行sql
  mycursor.execute(sql)
  # 判斷是否已經登入
  flag = False
  for x in mycursor:
    if x[0] != 0:
       flag = True
  if flag == True:
    session.permanent = True
    session["name"] = name
    return redirect('/member')
  else:
    return redirect("/error?message=登入錯誤")


# 登出api
@app.route("/logout")
def logoutHandler():
  # 刪除session
  session.pop("name",None)
  return redirect('/')



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