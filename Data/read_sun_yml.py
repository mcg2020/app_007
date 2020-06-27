import yaml

sum_list = []

with open("./sum.yml", "r") as f:
    data = yaml.safe_load(f)
    print("data:", data)
    # print("values:",data.values()) # 返回列表 存储所有value
    for i in data.values():
        # print("tup:", (i.get("a"), i.get("b"), i.get("c")))
        # 添加元组数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))