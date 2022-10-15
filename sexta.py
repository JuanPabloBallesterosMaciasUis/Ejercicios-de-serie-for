n = int(input("Digite No. de elementos de la serie: "))
s = "Serie = "
for i in range (1,n+1):
    if i != n:
        i = 1 + i**2 
        s = s + str(i) + ","
    else:
        s = s + str(i)
print(s) 
i**i+i