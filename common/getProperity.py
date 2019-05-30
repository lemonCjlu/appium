import json
def getProperity(properity_path):
    #以json形式读取元素属性
    with open(properity_path, 'r') as fin:
        d = json.load(fin)
        return d

