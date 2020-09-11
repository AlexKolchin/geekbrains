m = 'меня видно везде'

def a():
    ma = 'Меня видно в b() и в (a)'

    def b():
        print(m)
        print(ma)
        mb = 'меня видно в c() и в b() но не видно в a()'

        def c():
            print(m)
            print(ma)
            print(mb)

            mc = 'меня видно только в c()'

        # print(mc)
        c()

    b()

a()