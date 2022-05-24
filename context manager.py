class NotChangeList:

    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [1, 2]

try:
    with NotChangeList(v1) as ch:
        for index, el in enumerate(ch):
            ch[index] += v2[index]
except:
    print('Error')

print(v1)
