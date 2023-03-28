def parola_check(parola_string: str) -> int:
    #verific cate probleme are parola (lipsa cifra, lowercase si uppercase)
    ok1 = ok2 = ok3 = True
    nr_probleme = 0
    n=len(parola_string)
    for i in range(n):
        if parola_string[i].isdigit() and ok1:
            nr_probleme += 1
            ok1=False
        elif parola_string[i].islower() and ok2:
            nr_probleme += 1
            ok2=False
        elif parola_string[i].isupper() and ok3:
            nr_probleme += 1
            ok3=False

    nr_probleme = 3 - nr_probleme
    print("PROBLEME INITIALE: ",nr_probleme)

    #case len<6: cate mai avem de adaugat ca sa facem len minima vs cate trebuie adaugate ca sa indeplineasca cerintele
    if n < 6:
        return max(nr_probleme, 6-n)
    
    #acum ne legam de grupuri de litere consecutive (len>2) si le punem intr-un sir
    grupuri = []
    sir_curent = []
    chr_curent = parola_string[0]
    for i in range(n-1):
        if parola_string[i].isalpha() and parola_string[i] == parola_string[i+1]:
            sir_curent.append(parola_string[i])
            chr_curent = parola_string[i]
        else:
            sir_curent.append(chr_curent)
            if len(sir_curent) > 2:
                grupuri.append(sir_curent)
            sir_curent = []

    if chr_curent == parola_string[n-1]:
        sir_curent.append(parola_string[n-1])
        if len(sir_curent) > 2:
            grupuri.append(sir_curent)

    #print(grupuri)

    #case len>20: eliminam cate un caracter din grupurile de litere consecutive (len>2) pana cand len=20
    #prima data eliminam din grupurile de multiplu de 3 (cate un chr), apoi cate 2 din multiplu de 3 +1, apoi cate 3 din multimplu de 3 +2
    #daca nu merge pe niciun caz (nu mai avem destule litere ramase) eliminam random, nu are importanta oricum (nu se mai produc modificari)
    #daca len>20 si nu mai avem grupuri de litere consecutive (len>2) eliminam cate un caracter din parola

    #break the grupuri into 3 groups: len%3==0, len%3==1, len%3==2
    grupuri_0 = []
    grupuri_1 = []
    grupuri_2 = []
    for i in range(len(grupuri)):
        if len(grupuri[i]) % 3 == 0:
            grupuri_0.append(grupuri[i])
        elif len(grupuri[i]) % 3 == 1:
            grupuri_1.append(grupuri[i])
        else:
            grupuri_2.append(grupuri[i])

    if n>20:
        while n>20:
            if len(grupuri_0) > 0:
                grupuri_0[0].pop(0)
                n -= 1
                if len(grupuri_0[0]) < 3:
                    grupuri_0.pop(0)
                else:
                    grupuri_2.append(grupuri_0[0])
                    grupuri_0.pop(0)
            elif len(grupuri_1) > 0:
                grupuri_1[0].pop(0)
                n-=1
                if n>20:
                    grupuri_1[0].pop(0)
                    n-=1
                if len(grupuri_1[0]) < 3:
                    grupuri_1.pop(0)
                else:
                    grupuri_2.append(grupuri_1[0])
                    grupuri_1.pop(0)
            elif len(grupuri_2) > 0:
                grupuri_2[0].pop(0)
                n-=1
                if n>20:
                    grupuri_2[0].pop(0)
                    n -= 1
                if n>20:
                    grupuri_2[0].pop(0)
                    n-=1
                if len(grupuri_2[0]) < 3:
                    grupuri_2.pop(0)
            else:
                n -= 1

    #verific cate probleme mai are parola dupa eliminarile facute
    probleme_ramase=0
    for i in range(len(grupuri_0)):
        probleme_ramase+=len(grupuri_0[i])//3
    for i in range(len(grupuri_1)):
        probleme_ramase+=len(grupuri_1[i])//3
    for i in range(len(grupuri_2)):
        probleme_ramase+=len(grupuri_2[i])//3

    if len(parola_string)>20:
        return max(nr_probleme,probleme_ramase+(len(parola_string)-20))
    else:
        return max(nr_probleme,probleme_ramase)

print(parola_check("a"))
print(parola_check("aA1"))
print(parola_check("1337C0d3"))
print(parola_check("aaaB1"))
print(parola_check("aaa123"))
print(parola_check("bbaaaaaaaaaaaaaaacccccc"))
print(parola_check("aaabbbbdddcccc"))
print(parola_check("..."))
print(parola_check("...aa...a..."))
