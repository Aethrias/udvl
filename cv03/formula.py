class Formula(object):
    def __init__(self, subformulas):
        self.sub = subformulas
    def eval(self, i):
        pass
    def toString(self):
        pass
    def subf(self):
        return self.sub

class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self, [])
        self.name = name
    def eval(self, i):
        return i[self.name]
    def toString(self):
        return self.name

class Negation(Formula):
    def __init__(self, form):
        Formula.__init__(self, [form])
    def originalFormula(self):
        return self.subf()[0]
    def eval(self, i):
        return not self.originalFormula().eval(i)
    def toString(self):
        return "-" + self.originalFormula().toString()

class Conjunction(Formula):
    def __init__(self, form):
        Formula.__init__(self, form)
    def eval(self, i):
        vysledok = True
        for subformulas in self.subf(): 
            vysledok = vysledok and subformulas.eval(i) 
        return vysledok 
    def toString(self):
        return "(" + '&'.join([form.toString() for form in self.subf()]) + ")"

class Disjunction(Formula):
    def __init__(self, form):
        Formula.__init__(self, form)
    def eval(self, i):
        vysledok = False
        for subformulas in self.subf(): 
            vysledok = vysledok or subformulas.eval(i) 
        return vysledok 
    def toString(self):
        return "(" + '|'.join([form.toString() for form in self.subf()]) + ")"
   
class Implication(Formula):
    def __init__(self, form1, form2):
        Formula.__init__(self, [form1, form2])
    def eval(self, i):
        vysledok = True
        for subformulas in self.subf(): 
            vysledok = (not vysledok) or subformulas.eval(i) 
        return vysledok 
    def toString(self):
        return "(" + '=>'.join([form.toString() for form in self.subf()]) + ")"

class Equivalence(Formula):
    def __init__(self, form1, form2):
        Formula.__init__(self, [form1, form2])
    def eval(self, i):
        return self.subf()[0].eval(i) == self.subf()[1].eval(i) 
    def toString(self):
        return "(" + '<=>'.join([form.toString() for form in self.subf()]) + ")"
