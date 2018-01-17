# -*- coding:utf-8 -*-

# nums = [11, 22, 33, 44, 55]
nums = []
# for num in nums:
#     print(num)

# for循环的else
# for temp in nums:
#     print(temp)
#     break
# else:
#     print("======")


#名片管理器
infoCards = [{
    "name": "jack",
    "age": 19
}, {
    "name": "lisi",
    "age": 20
}, {
    "name": "rose",
    "age": 18
}]

findName = input("请输入要查询的名字:")

print(findName)

for temp in infoCards:
    if temp['name'] == findName:
        print("找到了")
        break
else:
    print("查无此人……")


