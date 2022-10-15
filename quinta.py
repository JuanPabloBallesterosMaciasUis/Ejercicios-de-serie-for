n = int(input("Digite No. de elementos de la serie: "))
s = "Serie = "
for i in range (1,n+1):
    if i != n:
        i = i**2+1 
        i = "1/" + str(i)
        s = s + str(i) + ","
    else:
        i = "1/" + str(i)
        s = s + str(i)
print(s) 