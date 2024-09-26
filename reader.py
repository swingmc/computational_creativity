import json
import os

class Poem:
    def __init__(self, title, author, lines):
        self.title = title
        self.author = author
        self.lines = lines

# 构建文件路径
file_path = os.path.join(os.getcwd(), 'poetry', 'poem.json')

# 读取和解析JSON文件
with open(file_path, 'r') as f:
    data_dict = json.load(f)

poem = Poem(**data_dict)

print(poem.title)
print(poem.author)
print(poem.lines)