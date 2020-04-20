def conjecture(number,array):
    array.append(number)    
    if number == 1:
        for elem in array:
            print(elem)
    else:
        if number % 2 == 0:
            conjecture(number//2,array)
        else:
            conjecture((3*number)+1,array)
            
a = []
conjecture(int(input('Enter a number:\n')),a)
