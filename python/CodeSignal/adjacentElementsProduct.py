def solution(inputArray):
    i = 0
    product = 0
    while i < (len(inputArray) - 1):
        multiplied = inputArray[i] * inputArray[i + 1]
        if i == 0:
            product = multiplied
        elif multiplied > product:
            product = multiplied
        i += 1
    return product