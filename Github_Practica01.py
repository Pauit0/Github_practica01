def triangle(): # 2 Pau A
    h = float(input("Quan mesura l'altura?"))
    a = float(input("Quan mesura un costat?"))
    b = float(input("Quan mesura la base?"))
    c = float(input("Quan mesura el costat que falta?"))
    area = b*h/2
    perimetre = a+b+c
    return area, perimetre
######################################################################