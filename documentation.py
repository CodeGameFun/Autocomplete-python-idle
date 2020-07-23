alphabets_str = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,_'
alphabets_list = alphabets_str.split(',')  #alphabets in list

functions_str = 'abs(), delattr(), hash(), memoryview(), set(), all(), dict(), help(), min(), setattr(), any(), dir(), hex(), next(), slice(), ascii(), divmod(), id(), object(), sorted(), bin(), enumerate(), input(), oct(), staticmethod(), bool(), eval(), int(), open(), str(), breakpoint(), exec(), isinstance(), ord(), sum(), bytearray(), filter(), issubclass(), pow(), super(), bytes(), float(), iter(), print(), tuple(), callable(), format(), len(), property(), type(), chr(), frozenset(), list(), range(), vars(), classmethod(), getattr(), locals(), repr(), zip(), compile(), globals(), map(), reversed(), __import__(), complex(), hasattr(), max(), round()'
functions_list = functions_str.split('(), ')  #functions in list

global doc
doc = {  #empty dictionary

}

for alphabet in alphabets_list:  #sorting the functions according to alphabets (first letter) in doc
    func = []  
    for function in functions_list:
        if function[0] == alphabet:
            func.append(function)
        else:
            doc[alphabet] = func



# How to add more library:
# 1. Make a list of the category items
# 2. Create another dictionary or add a dictionary in doc
# 3. Copy the 'Sorting' code
# 4. Change values

# Librarary Ref = https://docs.python.org/3/library/index.html

# CodeGameFun's Autocomplete specially for IDLE users