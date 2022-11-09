print("""*************************
Taschenrechner Programm

Rechenzeichen:

1. Addieren

2. Subtrahieren

3. Multiplizieren

4. Dividieren
*************************
""")

a = int (input("1. Zahl:"))
b = int (input("2. Zahl:"))

Rechenzeichen=input("Rechenzeichen eingeben:")

if Rechenzeichen=="1":
    print("{} plus {} ergibt gleich {}".format(a,b,a+b))
elif Rechenzeichen == "2":
        print("{} minus {} ergibt gleich {}".format(a, b, a - b))
elif Rechenzeichen=="3":
    print("{} mal {} ergibt gleich {}".format(a,b,a * b))
elif Rechenzeichen=="4":
    print("{} geteilt durch {} ergibt gleich {}".format(a,b,a / b))
else:
    print("Eingabe Ungültig")
    
