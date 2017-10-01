import os
import re


dir_ = os.listdir()
while dir_:
    a=dir_.pop()
    p.compile(r".*\..*")
    if p.findall(a)
		    f = open(a,'r')
		    b = bytes(f.read(),encode('utf-8'))
		    f.close()
		    f = open(a,'wb')
		    f.write(b)
		    f.close()
    else:
				chdir(r'.' + os.sep +a)
        dir_ = os.listdir()
