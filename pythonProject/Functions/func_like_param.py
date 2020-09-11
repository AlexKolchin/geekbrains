def f():
    print('hello from other f')

def to(f_param):
    # параметром будет функция
    # поэтому в теле функции to мы её вызовем
    f_param()

# проверим
to(f)