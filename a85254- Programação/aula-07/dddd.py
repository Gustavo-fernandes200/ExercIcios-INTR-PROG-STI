def outer_function():
    global a


    def inner_function():
        global a
        a = 30
        print('a_i =', a)

    inner_function()
    a = 20
    print('a_o =', a)


a = 10
outer_function()
print('a_M =', a)
