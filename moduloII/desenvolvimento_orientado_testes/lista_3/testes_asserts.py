num = 3
for i in range(2,num+1):
        if i*i <= num and num % i == 0:
            sum += i
            if i*i != num:
                sum += num/i
        i += 1

print(sum)