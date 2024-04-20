# -*- coding: utf-8 -*-
"""
Integral Expression
Monomial
Polynomial 
"""

from pymath.algebra.algebraicexpression import AlgebraicExpression
from pymath.numbertheory.number_theory import fact

#Class Polynomial
class poly(AlgebraicExpression) :
    """Polynomial"""
    def __init__(self,polystr:str):
        self.coeflist = []
        self.deglist = []
        self.variable = []
        self.str_ = polystr
        lstrt = polystr.split("+")
        for term in lstrt :
            termlist = term.split('*')
            for substr in termlist :
                if substr == '' :
                    termlist.remove(substr)
            try :
                self.coeflist.append(float(termlist[0]))
            except ValueError :
                self.coeflist.append(termlist[0])
            for i in range(1,len(termlist)):
                stri = termlist[i]
                if stri.isalpha() :
                    self.variable.append(stri)
                elif stri != '' :
                    try :
                        self.deglist.append(float(stri))
                    except Exception :
                        self.deglist.append(stri)

    @classmethod
    def from_list(cls,coefs:list,degs:list):
        polyr = poly("")
        polyr.coeflist = coefs
        polyr.deglist = degs
        polyr.variable = ["x"]
        listrtype2 = []
        strtype2init = "{}*x**{}+"
        for k in range(0,len(coefs)):
            listrtype2.append(strtype2init.format(coefs[k],degs[k]))
        strtype2i = listrtype2[0]
        for i in range(1,len(listrtype2)):
            strtype2i += listrtype2[i]
        strtype2 = strtype2i[:-1]
        polyr.str_ = strtype2
        return polyr
    
    #Classmethod
    def from_mono_terms(list_of_terms:list):
        lt = list_of_terms
        lstrs = []
        for term in lt :
            lstrs.append(str(term))
        strinit = ""
        for i in range(0,len(lstrs)):
            strinit = strinit+lstrs[i]+"+"
        strpoly = strinit[:-1]
        pr = poly(strpoly)
        return pr
    
    #Classmethod
    def to_int_or_float(self):
        list0 = [0 for n in range(self.numterm)]
        d = self.deglist
        if d == list0 :
            floatr = sum(self.coeflist)
            return floatr
    
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
        return len(list(set(self.variable)))
    
    #Variables
    @property
    def var(self):
        lr = list(set(self.variable))
        return lr
    
    #Degree 
    @property
    def degree(self):
        if self.ismono == False :
            return max(self.deglist)
        if self.ismono == True :
            if self.numvar == 1 :
                return max(self.deglist)
            if self.numvar > 1 :
                return sum(self.deglist)

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
            return [self]
        if self.ismono == False :
            polystr = self.str_
            listterms = polystr.split("+")
            listr = []
            for string in listterms :
                listr.append(poly(string))
            return listr

    def isliketerm(self,mono2):
        if self.ismono == True :
            if isinstance(mono2,poly) and mono2.ismono == True :
                deg1 = self.deglist
                deg2 = mono2.deglist
                var1 = self.variable
                var2 = mono2.variable
                l1 = list(zip(var1,deg1))
                l2 = list(zip(var2,deg2))
                listbool = []
                for t1 in l1 :
                    if t1 in l2 :
                        listbool.append('True')
                    else :
                        listbool.append('False')
                if 'False' not in listbool :
                    return True
                else :
                    return False
    
    #Combine like terms
    def combine_liketerms(mono1,mono2):
        if isinstance(mono1,poly) and isinstance(mono2,poly) :
            if mono1.ismono == True and mono2.ismono == True :
                if mono1.isliketerm(mono2):
                    c1 = mono1.coeflist[0]
                    c2 = mono2.coeflist[0]
                    c = c1+c2
                    strr = mono1.str_
                    strcoef = strr.split('*')[0]
                    strr = strr.replace(strr[0:len(strcoef)],str(c),1)
                    pr = poly(strr)
                    return pr
                
    #Ascending Powers
    def ascp(self,variable:str):
        lt = self.terms
        for j in range(0,len(lt)-1):
            for i in range(0,len(lt)-1):
                term1 = lt[i]
                term2 = lt[i+1]
                st1 = str(term1)
                st2 = str(term2)
                split1 = st1.split("*")
                split2 = st2.split("*")
                if variable in split1 :
                    if variable in split2 :
                        ind1 = split1.index(variable)
                        deg1 = float(split1[ind1+2])
                        ind2 = split2.index(variable)
                        deg2 = float(split2[ind2+2])
                        if deg1 > deg2 :
                            lt[i] = term2
                            lt[i+1] = term1
        lstrs = []
        for term in lt :
            lstrs.append(str(term))
        strinit = ""
        for i in range(0,len(lstrs)):
            strinit = strinit+lstrs[i]+"+"
        strpoly = strinit[:-1]
        pr = poly(strpoly)
        return pr
    
    #Descending Powers
    def dscp(self,variable:str):
        lt = self.terms
        for j in range(0,len(lt)-1):
            for i in range(0,len(lt)-1):
                term1 = lt[i]
                term2 = lt[i+1]
                st1 = str(term1)
                st2 = str(term2)
                split1 = st1.split("*")
                split2 = st2.split("*")
                if variable in split1 :
                    if variable in split2 :
                        ind1 = split1.index(variable)
                        deg1 = float(split1[ind1+2])
                        ind2 = split2.index(variable)
                        deg2 = float(split2[ind2+2])
                        if deg1 < deg2 :
                            lt[i] = term2
                            lt[i+1] = term1
        lstrs = []
        for term in lt :
            lstrs.append(str(term))
        strinit = ""
        for i in range(0,len(lstrs)):
            strinit = strinit+lstrs[i]+"+"
        strpoly = strinit[:-1]
        pr = poly(strpoly)
        return pr
            
    #To-Function
    @property
    def polyfunction(self):
        var = self.var
        strvars = ""
        for i in range(0,len(var)-1):
            strvars = strvars+var[i]+","
        strvars = strvars+var[-1]
        polystr = self.str_
        funcstr = "lambda "+strvars+" :"+" "+polystr
        f = eval(funcstr)
        return f
                
    #Evaluate
    def polyeval(self,dictvar:dict):
        polystr = self.str_
        for substr in polystr :
            if substr.isalpha() :
                num = dictvar[substr]
                polystr = polystr.replace(substr,str(num))
        result = eval(polystr)
        return result
    
    #Simplify
    def simplify(self):
        terms = self.terms
        for t in terms :
            if t.coeflist[0] == 0 :
                terms.remove(t)
            if len(t.var) != len(t.variable) :
                c = t.coeflist[0]
                d = t.deglist
                tindex = terms.index(t)
                dr = sum(d)
                v = t.var[0]
                sn = "{}*{}**{}".format(c,v,dr)
                tn = poly(sn)
                terms[tindex] = tn
            if 0.0 in t.deglist :
                vs = t.variable
                ds = t.deglist
                lists = list(zip(vs,ds))
                listn = []
                for tup in lists :
                    if tup[1] != 0.0 :
                        listn.append(tup)
                strcoef = "{}*".format(t.coeflist[0])
                strinit = "{}**{}*"
                lstrs = []
                for tupn in listn :
                    vn = tupn[0]
                    dn = tupn[1]
                    strn = strinit.format(vn,dn)
                    lstrs.append(strn)                   
                strpoly = ""
                for substr in lstrs :
                    strpoly = strpoly+substr
                strpoly = strcoef+strpoly
                strpoly = strpoly[:-1]
                tr = poly(strpoly)
                tindex = terms.index(t)
                terms[tindex] = tr
        n = len(terms)
        listr = []
        lliketerms = []
        termsnew = []
        termsremove = []
        for j in range(0,n-1):
            inum = terms[j]
            newl = terms[j+1:]
            for n in newl :
                listr.append((inum,n))
        for tup in listr :
            termi = tup[0]
            termn = tup[1]
            if termi.isliketerm(termn) :
                termc = poly.combine_liketerms(termi,termn)
                lliketerms.append(termc)
                termsremove.append(termi)
                termsremove.append(termn)
        for t in terms :
            if t not in lliketerms and t not in termsremove :
                termsnew.append(t)
        termsnew = termsnew+lliketerms
        liststrt = []
        for t in termsnew :
            liststrt.append(str(t))
        strinit = ""
        for strt in liststrt :
            strinit = strinit+strt+"+"
        strinit = strinit[:-1]
        pr = poly(strinit)
        return pr
    
    #Factorization
    def factor(self):
        if self.ismono == True :
            v = self.variable
            d = self.deglist
            c = self.coeflist[0]
            l = list(zip(v,d))
            liststrs = []            
            for tup in l :
                var = tup[0]
                deg = tup[1]
                strterm = "{}*{}**{}".format(c,var,deg)
                liststrs.append(strterm)
            listfactors = []
            for substr in liststrs :
                listfactors.append(poly(substr))
            list1 = []
            listextend = []
            for factor in listfactors :
                times = int(factor.degree)
                variable = factor.var[0]
                strnew = "{}*{}**1.0".format(1.0,variable)
                factornew = poly(strnew)
                lex = [factornew for n in range(0,times)]
                listextend = listextend+lex
            listfactors = list1+listextend
            listnumfactors = fact(c)
            lnfn = []
            for num in listnumfactors :
                if num != 1 and num != -1 :
                    lnfn.append(num)
            listfactors = lnfn+listfactors
            return listfactors
        if self.ismono == False :
            t = self.terms
            listfactorsstrset = []
            for term in t :
                lf = term.factor()
                lfs = [str(p) for p in lf]
                lsfset = set(lfs)
                listfactorsstrset.append(lsfset)
            for i in range(0,len(listfactorsstrset)-1):
                setstr1 = listfactorsstrset[i]
                setstr2 = listfactorsstrset[i+1]
                setintersection = setstr1.intersection(setstr2)
                listfactorsstrset[i+1] = setintersection
            setinterall = listfactorsstrset[-1]
            interall = list(setinterall)
            listcommonfactors = []
            for substr in interall :
                listcommonfactors.append(poly(substr))
            listquots = []
            for factor_ in listcommonfactors :
                for term_ in t :
                    quot = divmod(term_,factor_)[0]
                    if isinstance(quot,poly) :
                        quot = quot.simplify()
                        listquots.append(quot)
            polyquot = poly.from_mono_terms(listcommonfactors)
            polymul = poly.from_mono_terms(listquots)
            polyquot = polyquot.simplify()
            polymul = polymul.simplify()
            quotstr = str(polyquot)
            mulstr = str(polymul)
            strmul = "*({})".format(mulstr)
            result = AlgebraicExpression(quotstr+strmul)
            return result
        
    def __eq__(self,poly2):
        if isinstance(poly2,poly):
            p1 = self.dscp('x')
            p2 = poly2.dscp('x')
            if str(p1) == str(p2) :
                return True
            else :
                return False
            
    def __ne__(self,poly2):
        if isinstance(poly2,poly):
            p1 = self.dscp('x')
            p2 = poly2.dscp('x')
            if str(p1) == str(p2) :
                return False
            else :
                return True
            
    #Polynomial Addition
    def __add__(self,poly2):
        if isinstance(poly2,poly):
            t1 = self.terms
            t2 = poly2.terms
            listliketerms = []
            for p in t1 :
                for p2 in t2 :
                    if p.isliketerm(p2) :
                        listliketerms.append((p,p2))
            lt1 = [listliketerms[n][0] for n in range(0,len(listliketerms))]
            lt2 = [listliketerms[n][1] for n in range(0,len(listliketerms))]
            lun1 = []
            lun2 = []
            for term1 in t1 :
                if term1 not in lt1 :
                    lun1.append(term1)
            for term2 in t2 :
                if term2 not in lt2 :
                    lun2.append(term2)
            lun = lun1+lun2
            lcomb = []
            for t in listliketerms :
                m1 = t[0]
                m2 = t[1]
                mr = poly.combine_liketerms(m1,m2)
                lcomb.append(mr)
            lr = lun+lcomb
            strinit = ""
            for p in lr :
                strinit += str(p)+"+"
            strinit = strinit[:-1]
            pr = poly(strinit)
            return pr
            
    #Negative (-p:p:poly)
    def __neg__(self):
        lt = self.terms
        ltn = []
        for t in lt :
            c = t.coeflist[0]
            cr = -c
            s = t.str_
            ind = s.find("*")
            sn = s[ind:]
            scr = str(cr)
            sn = scr+sn
            tn = poly(sn)
            ltn.append(tn)
        pr = poly.from_mono_terms(ltn)
        return pr
    
    #Polynomial Subtraction
    def __sub__(self,poly2):
        if isinstance(poly2,poly):
            polyn = -poly2
            return self+polyn
        
    #Polynomial Multiplication
    def __mul__(self,poly2):
        if isinstance(poly2,poly):
            t1 = self.terms
            t2 = poly2.terms
            lstrs = []
            for mono1 in t1 :
                for mono2 in t2 :
                    c1 = mono1.coeflist[0]
                    c2 = mono2.coeflist[0]
                    cr = c1*c2
                    d1 = mono1.deglist
                    d2 = mono2.deglist
                    var1 = mono1.variable
                    var2 = mono2.variable
                    l1 = list(zip(var1,d1))
                    l2 = list(zip(var2,d2))
                    listr = []
                    listd1 = []
                    listd2 = []
                    for i in range(0,len(l1)):
                        for j in range(0,len(l2)):
                            tup1 = l1[i]
                            tup2 = l2[j]
                            if tup1[0] == tup2[0] :
                                tupr = (tup1[0],tup1[1]+tup2[1])
                                listr.append(tupr)
                                listd1.append(tup1)
                                listd2.append(tup2)
                    setd1 = set(listd1)
                    set1 = set(l1)
                    setd2 = set(listd2)
                    set2 = set(l2)
                    setr1 = set1.difference(setd1)
                    setr2 = set2.difference(setd2)
                    lr1 = list(setr1)
                    lr2 = list(setr2)
                    lr = listr+lr1+lr2
                    listvarr = []
                    listdegr = []
                    for i in range(0,len(lr)):
                        tup = lr[i]
                        listvarr.append(tup[0])
                        listdegr.append(tup[1])
                    strinit = ""
                    strinit = strinit+str(cr)+"*"
                    for j in range(0,len(listvarr)):
                        ssradd = "{}**{}*".format(listvarr[j],listdegr[j])
                        strinit = strinit+ssradd
                    strinit = strinit[:-1]
                    lstrs.append(strinit)
            polystr = ""
            for i in range(0,len(lstrs)-1):
                polystr = polystr+lstrs[i]+"+"
            polystr = polystr+lstrs[-1]
            pr = poly(polystr)
            pr = pr.simplify()
            return pr
                
    #Polynomial Power
    def __pow__(self,exp):
        p = poly(self.str_)
        liste = [p for n in range(0,exp)]
        p0 = liste[0]
        for i in range(1,len(liste)) :
            p0 = p0*liste[i]
        return p0
    
    #Polynomial Division
    def __divmod__(self,poly2):
        if isinstance(poly2,poly):
            if self == poly2 :
                return poly("1*x**0"),0
            if poly2.ismono == True :
                if self.ismono == True :
                    polydividend = self.simplify()
                    polydivisor = poly2.simplify()
                    v1 = polydividend.variable
                    d1 = polydividend.deglist
                    list1 = list(zip(v1,d1))
                    c1 = polydividend.coeflist[0]
                    v2 = polydivisor.variable
                    d2 = polydivisor.deglist
                    list2 = list(zip(v2,d2))
                    c2 = polydivisor.coeflist[0]
                    cr = c1/c2
                    listr = []
                    for tup1 in list1 :
                        var = tup1[0]
                        for tup2 in list2 :
                            if var == tup2[0] :
                                deg1 = tup1[1]-tup2[1]
                                tupr = (var,deg1)
                                listr.append(tupr)
                            if var not in v2 :
                                tupr = (var,tup1[1])
                                listr.append(tupr)
                    strf = "{}**{}*"
                    lstrs = []
                    for t in listr :
                        strn = strf.format(t[0],t[1])
                        lstrs.append(strn)
                    strc = "{}*".format(cr)
                    strr = ""
                    for substr in lstrs :
                        strr = strr+substr
                    strr =strc+strr
                    strr = strr[:-1]
                    pr = poly(strr)
                    pr = pr.simplify()
                    return pr,0
                if self.ismono == False :
                    t = self.terms
                    listquots = []
                    for mono in t :
                        quot = divmod(mono,poly2)[0]
                        listquots.append(quot)
                    polyquot = poly.from_mono_terms(listquots)
                    return polyquot
            if poly2.ismono == False :
                termsdividend = self.terms
                polydivisor = poly2
                polydividend = poly.from_mono_terms(termsdividend[0:poly2.numterm])
                listquot = []
                listreminder = []
                for i in range(0,self.numterm // poly2.numterm+1):
                    try :
                        nextterm = poly.from_mono_terms(termsdividend[i+poly2.numterm:])
                        mdend = polydividend.terms[0]
                        mdivis = polydivisor.terms[0]
                        mq = divmod(mdend,mdivis)[0]
                        listquot.append(mq)
                        md = polydividend - mq*polydivisor
                        md = md.simplify()
                        listreminder.append(md)
                        polydividend = md + nextterm
                        termsdividend = polydividend.terms
                    except IndexError :
                        for j in range(poly2.numterm):
                            mdend = polydividend.terms[0]
                            mdivis = polydivisor.terms[0]
                            mq = divmod(mdend,mdivis)[0]
                            listquot.append(mq)
                            md = polydividend - mq*polydivisor
                            md = md.simplify()
                            listreminder.append(md)
                polyquot = poly.from_mono_terms(listquot)
                polyreminder = poly.from_mono_terms([listreminder[-1]])
                return polyquot,polyreminder
        if isinstance(poly2,int) or isinstance(poly2,float) :
            pstr = "{}*x**0".format(poly2)
            poly2 = poly(pstr)
            return divmod(self,poly2)
                
