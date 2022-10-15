n = int(input("Digite No. de elementos de la serie: "))
s = "Serie = "
for i in range (1,n+1):
    if i != n:
        i = 3+(i-1)*5 
        s = s + str(i) + ","
    else:
        i = 3+(i-1)*5 
        s = s + str(i)
print(s) 
#5i-2
