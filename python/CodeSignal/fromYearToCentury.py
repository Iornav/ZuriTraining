import math
def solution(year):
    if year >=1 and year <=2005:
        if year%100 == 0:
            century = year/100
            print(century)
            return(century)
        else:
            century = math.floor(year/100) + 1
            print(century)
            return(century)    
solution(1709)