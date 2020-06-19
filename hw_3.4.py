#option1

def func(x, y):
    z = x ** y
    print(z)

func(5, -5)

#option2

def func(x, y):

    counter = -y
    current = 1

    while counter > 0:
        current /= x
        counter -= 1
    print(current)


func(5, -5)