import os
import os.path

#文件操作 之目录
fileNames = os.listdir("D:\work4bs")

for name in fileNames:
    # if os.path.isfile(name) == True:
    print(name)
else:
    print("没有结果")
    # name.