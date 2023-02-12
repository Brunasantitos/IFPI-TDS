def fatorial(f):
 fat = 1

 for i in range (1,f+1):
    
    fat = fat * i
 return fat

num = int(input("\nDigite um número: "))
print("\nO fatorial de %d é: %d" % (num, fatorial(num)))
