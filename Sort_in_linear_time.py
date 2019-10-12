

class ksort:
    def __init__(self):
        self.first_symbol=['a','b','c','d','e','f','g','h']
        self.secont_and_third_symbol=["1","2","3","4","5","6","7","8","9","0"]
        self.size=len(self.first_symbol)*len(self.secont_and_third_symbol)**2
        self.const=10228
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
        data_indexes=self.index(s)
        if data_indexes==-1:
            return False
        else:
            if self.items[data_indexes]==None:
                #self.items[data_indexes[i]]=s[i]
                self.items[data_indexes]=1
            else:
                self.items[data_indexes]+=1
        return True


    def index(self,s):
        #Метод вычесляет индекс в массиве
        s=self.IsItRightString(s)
        if s==-1:
            return -1
        else:
            len_s=len(s)
            out_index=[]
            for i in range(0,len_s):
                index_number=0
                for j in range(0,len(s[i])):
                    index_number=index_number+ord(s[i][j])*(10**(2-j))
                index_number=index_number-self.const
                out_index=index_number
        return out_index
"""
Z=ksort()
s="a00"
print(Z.index(s))

print(Z.add(s))
print(Z.items)
"""


