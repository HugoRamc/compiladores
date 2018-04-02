precedencia = {}
precedencia["("] = 1
precedencia[")"] = 1
precedencia["s"] = 2
precedencia["c"] = 2
precedencia["t"] = 2
precedencia["^"] = 3
precedencia["r"] = 3
precedencia["*"] = 4
precedencia["/"] = 4
precedencia["+"] = 5
precedencia["-"] = 5

def sufija(cadena):
    salida = []
    pilaOperadores = []
    for c in cadena:
        aux = ord(c)
        if 48<=aux<=57 or c == "e" or c == "p":
            salida.append(c)
        else:
            if c == ")":
                aux = []
                bandera = True
                while bandera and pilaOperadores:
                    aux_c = pilaOperadores.pop()
                    if aux_c != "(":
                        aux.append(aux_c)
                    else:
                        bandera = False
                salida.extend(aux)
            elif c == "(":
                pilaOperadores.append(c)
            else:
                if pilaOperadores:
                    pre = precedencia[c]
                    pre_pila = precedencia[pilaOperadores[-1]]
                    if pre_pila <= pre and pre_pila!=1:
                        aux = []
                        o = ""
                        while pilaOperadores and o != "(":
                            o = pilaOperadores.pop()
                            if o != "(":
                                salida.append(o)
                        pilaOperadores.append(c)
                    else:
                        pilaOperadores.append(c)
                else:
                    pilaOperadores.append(c)
    while pilaOperadores:
        salida.append(pilaOperadores.pop())

    return salida

def prefija(cadena):
    salida = []
    pilaOperadores = []
    for i in range(len(cadena)):
        c = cadena[-1-i]
        aux = ord(cadena[-1-i])
        if 48<=aux<=57 or c == "e" or c == "p":
            salida.append(c)
        else:
            if c == "(":
                aux = []
                bandera = True
                while bandera and pilaOperadores:
                    aux_c = pilaOperadores.pop()
                    if aux_c != "(":
                        aux.append(aux_c)
                    else:
                        bandera = False
                salida.extend(aux)
            elif c == ")":
                pilaOperadores.append(c)
            else:
                if pilaOperadores:
                    pre = precedencia[c]
                    pre_pila = precedencia[pilaOperadores[-1]]
                    if pre_pila <= pre and pre_pila!=1:
                        aux = []
                        o = ""
                        while pilaOperadores and o != ")":
                            o = pilaOperadores.pop()
                            if o != "(":
                                salida.append(o)
                        pilaOperadores.append(c)
                    else:
                        pilaOperadores.append(c)
                else:
                    pilaOperadores.append(c)
    while pilaOperadores:
        salida.append(pilaOperadores.pop())

    return salida

def convertir_cadena(cadena):
    salida = []
    for c in cadena:
        salida.append(c)
    return salida

if __name__ == '__main__':
    cadena = "(1+2)*(3+4)"
    cadena = convertir_cadena(cadena)
    cadena1 = []
    salida = sufija(cadena)
    print(salida)
    salida1 = prefija(cadena)
    print(salida1)
