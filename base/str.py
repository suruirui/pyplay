str = 'hello python hello linux hellp ubuntu';

print(str.find('python')) #chazhao zifchuansuoyin
print(str.count('hello'));
print(str.capitalize()); 
print(str.title());
print(str.split(" "));
print(str.index("linux"));
print(str.startswith("linux"));
print(str.endswith("linux"));
print(str.upper());
print(str.lower());
print(str.rfind('python')); #6
print(str.rindex('linux')); #19


test1 = str.center(50)
test2 = str.ljust(50)
test3 = str.rjust(50)


print(test1);
print(test2);
print(test3);

print(test1.lstrip());
print(test2.rstrip());
print(test3.strip());

