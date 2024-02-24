# -*- coding: utf-8 -*-
"""
Integral Expression
Monomial
Polynomial 
"""
#Class Polynomial
class poly :
    """Polynomial"""
    def __init__(self,polystr:str):
        self.coeflist = []
        self.deglist = []
        self.variable = []
        self.str_ = polystr
        numlist = []
        for substr in polystr :
            if substr.isdigit() :
                numlist.append(float(substr))
            if substr.isalpha() :
                self.variable.append(substr)
        for i in range(0,len(numlist)):
            if i%2 == 0 :
                self.coeflist.append(numlist[i])
            if i%2 == 1 :
                self.deglist.append(numlist[i])

    @classmethod
    def from_list(cls,coefs:list,degs:list):
        polyr = poly("")
        polyr.coeflist = coefs
        polyr.deglist = degs
        polyr.variable = ["x"]
        listrtype2 = []
        strtype2init = "{}*x**{}+"
        for k in range(0,len(coef)):
            listrtype2.append(strtype2init.format(coef[k],deg[k]))
        strtype2i = listrtype2[0]
        for i in range(1,len(listrtype2)):
            strtype2i += listrtype2[i]
        strtype2 = strtype2i+"0"
        polyr.str_ = strtype2
        return polyr
        
    def __str__(self):
        return self.str_

    def __repr__(self):
        return str(self)

    def __list__(self):
        return self.coeflist

    #Properties
    #Number of variables
    @property
    def numvar(self):
        return len(self.variable)
    
    #Degree 
    @property
    def degree(self):
        return max(self.deglist)

    #Number of terms
    @property
    def numterm(self):
        return len(self.coeflist)
    
    @property
    #The constant term 
    def consterm(self):
        return self.coeflist[-1]

    #The coefficients 
    @property
    def coef(self):
        return self.coeflist
    
    #The exponents of terms 
    @property
    def deg(self):
        return self.deglist

    @property
    def ismono(self):
        lists = self.str_.split("+")
        if len(lists) == 1 and lists[0] == self.str_ :
            return True
        else :
            return False
        
    @property
    #Terms
    def terms(self):
        if self.ismono == True :
            return self.str_
        if self.ismono == False :
            polystr = self.str_
            listterms = polystr.split("+")
            return listterms

    def isliketerm(self,mono2):
        if self.ismono() == True :
            if isinstance(mono2,poly) and mono2.ismono() == True :
                un1 = self.numvar
                un2 = mono2.numvar
                deg1 = self.deglist
                deg2 = mono2.deglist
                if deg1 == deg2 and un1 == un2 :
                    return True
                else :
                    return False

    
        

    
    
        
