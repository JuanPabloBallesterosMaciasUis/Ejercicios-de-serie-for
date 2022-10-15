n = int(input("Digite No. de elementos de la serie: "))
s = "Serie = "
for i in range (1,n+1):
    if i != n:
        i = 2 ** i
        s = s + str(i) + ","
    else:
        s = s + str(i)
print(s)  