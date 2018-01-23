# -*- coding:utf-8 -*-

import re

line = 'hello123'
regStr = "^h.*2$"

# ^以x开头 $以x结尾
#. 表示任意字符 .*任意字符出现多次

if re.match(regStr,line):
    print("yes")

line2 = "boooooobbbbby123"
# regStr2 = ".*(b.*b).*"  #boooooob
regStr2 = ".*?(b.*b).*"  #
matchObj = re.match(regStr2,line2)
if matchObj:
    print(matchObj.group(1))


