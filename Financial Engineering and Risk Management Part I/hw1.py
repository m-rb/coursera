import pandas as pd
import numpy as np

class FixedIncome():

    def __init__(self):
        pass

    def annuity(self,r,n):
        self.ani = (1 - ((1+r) ** - n)) / r
        return self.ani

    def pv(self,p,r,n):
        pv = p / ((1+r) ** n)
        return pv

    def fv(self,p,r,n):
        fv = p * (1+r) ** n
        return fv

    def question_1(self):
        principal = 500000#k
        r = 0.10 #yearly
        pv = principal + (principal * self.annuity(0.10,19))
        return round(pv,2) #2 decimals #dont forget to convert to millions

    def question_2(self):
        principal = [1000, 900]
        r = 0.12
        n = 6
        original_apartment_npv = - (principal[0] + principal[0] * self.annuity(r,n)) + self.pv(principal[0],r,n)
        new_apartment_npv = - (principal[0] + principal[1]) - (principal[1] + principal[1] * self.annuity(r,n-1)) + self.pv(principal[1],r,n)
        if original_apartment_npv > new_apartment_npv:
            solution = print('STAY')
        else:
            solution = print('LEAVE')
        return solution

    def question_3(self):
        s2 = 0.069
        discount_rate = 1 / (1+s2) ** 2
        return discount_rate

    def question_4(self):
        s1 = 0.063
        s2 = 0.069
        fwd = ((1+s2) ** 2) / ((1 + s1)) - 1
        return fwd

    def question_5(self):
        s0 = 400
        fwd_price = self.fv(s0,0.08/4,3)
        return fwd_price

    def question_6(self):
        rates = [0.10, 0.08]
        principal = 10000
        boundaries = [principal/i for i in rates]
        return boundaries[1] - boundaries[0]

    def question_7(self):
        forward_at_start = self.fv(100,0.1/2,2)
        current_price = 125
        current_fv = self.fv(current_price,0.1/2,1)
        return self.pv(current_fv-forward_at_start,0.1/2,1)



if __name__ == '__main__':
    object = FixedIncome()
    print(object.question_1())
    object.question_2()
    print(object.question_3())
    print(object.question_4())
    print(object.question_5())
    print(object.question_6())
    print(object.question_7())