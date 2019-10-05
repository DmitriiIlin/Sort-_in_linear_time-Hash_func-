

class ksort:
    def __init__(self):
        self.first_symbol=['a','b','c','d','e','f','g','h']
        self.secont_and_third_symbol=["1","2","3","4","5","6","7","8","9","0"]
        self.size=len(self.first_symbol)*len(self.secont_and_third_symbol)**2+9
        self.items=[None]*self.size

    def IsItRightString(self,s):
        #Проверка данных на корректность ввода
        s=str(s)
        s=(s.strip()).split(" ")
        s_len=len(s)
        for every_word in range(0,s_len):
            if len(s[every_word])==3:
                if s[every_word][0] in self.first_symbol and (s[every_word][1]) in self.secont_and_third_symbol and (s[every_word][2]) in self.secont_and_third_symbol:  
                    pass
                else:
                    return -1
            else:
                return -1
        return s
    
    def add(self,s):
        #Метод размещает строку s в массиве items в соответствующей позиции и возвращает true; а если строка некорректного формата, возвращает false
        s=self.IsItRightString(s)
        if s==-1:
            return False
        else:
            len_s=len(s)
            data_array=[]
            for i in range(0,len_s):
                data_array.append(sum(ord(s[i][j])**(3-j+1) for j in range(len(s[i])))%self.size)
            for hesh in range(0,len(data_array)):
                self.items[data_array[hesh]]=s[hesh]
        return True


    def index(self,s):
        #Метод вычесляет хеш входных данных s
        s=self.IsItRightString(s)
        if s==-1:
            return -1
        else:
            len_s=len(s)
            data_array=[]
            for i in range(0,len_s):
                data_array.append(sum(ord(s[i][j])**(3-j+1) for j in range(len(s[i])))%self.size)
        return data_array
"""
S="a00"
Z=ksort()
Z.add(S)
Z.add("d34")
print(Z.items)
"""


