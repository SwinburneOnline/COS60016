def scream(text):
    return text.upper()

print(scream('Hello!'))

yell = scream

print(yell('Hello'))



def scream(text):
    return text.upper()

def mutter(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

greet(scream)
greet(mutter)



def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))