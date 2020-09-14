import os

# Имя операционной системы
print(os.name)
# Текущая рабочая директория
print(os.getcwd())
# Создание нового пути
new_path = os.path.join(os.getcwd(), 'new_f')
# Создание папки по новому пути
os.mkdir(new_path)