import json

# 打开并读取 JSON 文件
with open('data.json', 'r') as file:
    data = json.load(file)

    # 一个简单的练习乐谱
with open('practice.json', 'r') as f:
    list = json.load(f)


keys = []
for item in list:
    keys.append(data[item])

print(keys)