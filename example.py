class Hello():

    def __init__(self):
        self.name = 'Tom'

    def say_hi(self):
        return print(f'hello {self.name}')

if __name__ == '__main__':
    hello = Hello()
    hello.say_hi()