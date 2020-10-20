import requests

# r = requests.get("https://www.baidu.com")
# r = requests.get("https://www.baidu.com")
# print(r.text)



score = int(input("请输入多少分："))
if score >= 80:
    print("优秀")
elif score >= 60 and score < 80:
    print("一般")
else:
    print("不及格")