s = 'Hello World Мир'
sb = s.encode('utf-8')

print(sb)
print(type(sb))

s = sb.decode('utf-8')
print(s)
print(type(s))