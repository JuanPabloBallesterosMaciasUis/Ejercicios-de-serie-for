n = int(input("Digite No. de elemots de la serie: "))
s = "Serie: "
for i in range (1,n+1):
    if i != n:
        s= s + str(i)   + ","
    else:
        s = s + str(i)
print(s) 

print("SEGUNDO EJERCICIO")
n1 = int(input("Digite No. de elemots de la serie: "))

s1 = "Serie: "
for i in range (1,n1+1):
    if i != n1:
        s1= s1 + i ** 2   + ","
    else:
        s1 = s1 + str(i)  
print(s1)
