# -*- coding:utf-8 -*-

#1.获取用户要复制的文件
oldPath = input("请输入要复制的文件名:")
# oldPath = "./test/ccc.txt"

#2.读取要复制的文件
oldFile = open(oldPath, "r")

position = oldPath.rfind(".")
newPath = oldPath[:position] + "[copy]" + oldPath[position:]

#新建一个文件
newFile = open(newPath, "w")

# 从旧文件中读取数据，并且写入到新文件中
while True:
    content = oldFile.read(1024)

    if len(content) == 0:
        break

    newFile.write(content)

print(oldPath)
print(newPath)
#5.关闭两个文件
oldFile.close()
newFile.close()