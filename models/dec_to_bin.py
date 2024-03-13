number = 101

result = [0,0,0,0,0,0,0,0]

def decimal_to_binary(num):
     
    i = 0
    while (num > 0):
        result[len(result)-1 - i] = num % 2
        num = num // 2
        i += 1

decimal_to_binary(number)
print(result)