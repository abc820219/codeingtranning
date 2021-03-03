# 請用你的程式補完這個函式的區塊avg({"count":3,"employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]})​ # 呼叫 avg 函式
def avg(data):
    result = 0
    for t in data["employees"]:
        result += t["salary"]
    print(result // len(data["employees"]))

avg({"count": 3, "employees": [{"name": "John", "salary": 30000}, {
    "name": "Bob", "salary": 60000}, {"name": "Jenny", "salary": 50000}]})
