# функция для создания файла

def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
