'''Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which 
the second occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.'''
def solution(a):
    new_a = set()
    
    for i in a:
        if i in new_a:
            print (i)
            return i
        else:
            new_a.add(i)
    if len(new_a) == len(a):
        return -1
solution([2, 1, 3, 1, 5, 6, 2])