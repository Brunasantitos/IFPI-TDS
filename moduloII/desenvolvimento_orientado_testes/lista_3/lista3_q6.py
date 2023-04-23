def isPerfectNumber(num):
    if type(num) == str:
        return Exception
    elif num <= 1: return False
    sum = 1
    for i in range(2,num+1):
        if i*i <= num and num % i == 0:
            sum += i
            if i*i != num:
                sum += num/i
        i += 1
    
    return sum == num

assert isPerfectNumber(8) == True
print("Testes ok.")