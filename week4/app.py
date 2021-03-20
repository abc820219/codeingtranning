from flask import Flask,request,redirect,render_template,session
from datetime import timedelta
app = Flask(
    __name__,
    static_folder = "static", #靜態資料夾
    static_url_path = "/" #對應的網址路徑
    ) # create app

# session密碼
app.secret_key = "hello"
# seesion持續時間
app.permanent_session_lifetime =  timedelta(minutes=5)

@app.route("/")
def index():
  print(session)
  if "isLogin" in session:
    return redirect('/member')
  return render_template('/index.html')


@app.route("/signin",methods=["POST"])
def siginHandler():
  account = request.form["account"]
  password = request.form["password"]
  if password == "test" and account == "test":
    # 啟用session持續時間
    session.permanent = True
    # 設定session狀態
    session["isLogin"] = True
    return redirect('/member')
  else:
    return redirect('/error')


@app.route("/logout")
def logoutHandler():
  # 刪除session
  session.pop("isLogin",None)
  return redirect('/')


@app.route("/member")
def index_home():
  return render_template('/member.html')

@app.route("/error")
def index_error():
  return render_template('/error.html')
  
app.run(port=3000)

#參考網址https://www.techwithtim.net/tutorials/flask/sessions/