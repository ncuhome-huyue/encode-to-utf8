import os
import re


dir_ = os.listdir()
while dir_:
    a = dir_.pop()
    p = re.compile(r".*\.txt")
    if p.findall(a):
        f = open(a,'r')
        b = f.read()
        b = b.encode('utf-8')
        f.close()
        f = open(a,'wb')
        f.write(b)
        f.close()
    else:
        os.chdir(r"." + os.sep + a)
        dir_ = os.listdir()
print('end')
        

