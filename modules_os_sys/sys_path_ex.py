# Мы можем импортировать
import math
# но не можем импортировать наш модуль например на диске С:
# import module

# как Python находит модуль?
import sys
print(sys.path)
print(type(sys.path))

for p in sys.path:
    print(p)
sys.path.append('C:\\Users\\okolc\\Desktop')
import mymodule