class foo:
    def __init__(self,nombrefuncion=None):
        self.nombreFuncion=nombrefuncion
        pass

    def eval(self,a,b):
        method = getattr(self,self.nombreFuncion)
        return method(a,b)

    def f1(self,str1,str2):
        aux = "f1 " + str1+ ' ' +str2
        print aux
        pass

    def f2(self,str1,str2):
        aux = "f2 " + str1+ ' ' +str2
        print aux
        pass

    def f3(self,str1,str2):
        aux = "f3 " + str1+ ' ' +str2
        print aux
        pass

f=foo('f1')
f.eval('hola123','321')

f=foo('f2')
f.eval('hola456','654')

f=foo('f3')
f.eval('hola789','987')