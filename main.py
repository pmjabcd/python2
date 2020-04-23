#만약 다른 파일에 있다면 파일명/mod1 이렇게 불러와야함#

import mod1
print(mod1.add(1.2))

from mod1 import add 
print(add(1.2))

from mod1 import *