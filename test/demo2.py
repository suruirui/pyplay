# -*- coding:utf-8 -*-

# 列表中的extend和append
a = [1,2,3]
b = [4,5]

# a.extend(b)  #[1, 2, 3, 4, 5]
#a.append(b)  #[1, 2, 3, [4, 5]]

a = a.append(b)  # *注意 append返回值为None
print(a)
