n = int(input("Se sumaran los numeros que ingrese asta que ingrese un 0...."))
i = int(1)
s = n
while(n != 0):
    n = int(input("Ingrese un 0 para terminar la suma"))
    i = i+1
    s = s+n

print("La suma es: ", s, "el total de numeros ingresados fue: ", i-1)