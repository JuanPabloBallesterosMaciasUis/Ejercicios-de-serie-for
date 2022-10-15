n = int(input("Digite el No. de elementos primos hasta los que quieres: "))
s = "Serie = "
for i in range (1,n):
    if i == 1 :
            s = s + "3" + ","
    if i != n:
        i = int((-(-1)**i + 6*i +3)/2)
        s = s + str(i) + "," 
    else:
        i = int((-(-1)**i + 6*i +3)/2)
        s = s + str(i)
print(s) 