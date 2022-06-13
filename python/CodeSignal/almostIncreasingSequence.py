def solution(sequence):
    length = len(sequence)
    count = 0
    for i in range(length -1):
        if sequence[-1]<= sequence [-2]:
            return False
        elif sequence[i]>= sequence[i+1] and sequence[i+2] > sequence[i]:
            sequence.pop(i+1)
            count+=1
            if count >1:
                return False
            else:
                return True
        else:
            return True    
    