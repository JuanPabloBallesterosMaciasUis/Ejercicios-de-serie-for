n = int(input("Digite No. de elementos de la serie: "))
s = "Serie = "
for i in range (1,n+1):
    if i != n:
        i2 =  i**(i-1)
        i = 3+(i-1)*2
        s = s + str(i2) + "/" + str(i) + ","
    else:
        i = 3+(i-1)*2 
        s = s + str(i2) + "/" + str(i)
print(s) 