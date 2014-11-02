## perceptron simple
def salida(k, pesos, t):
    print "SALIDA"
    print "-------"
    z=-t
    for i in range(len(k)):
        print "MOSTRANDO VALORES"
        print "z="+str(z)
        print "k["+str(i)+"]="+str(k[i])
        print "pesos["+str(i)+"]="+str(pesos[i])
        print "CALCULANDO Z"
        print "z=z+(k["+str(i)+"]*pesos["+str(i)+"])="+"="+str(z)+"+("+ \
        str(k[i])+"*"+str(pesos[i])+")=..."
        z=z+(k[i]*pesos[i])
        print str(z)
    if z>=0:
        print "z >= 0"
        print "retornando z = 1"
        print "-------"
        print "VOLVIENDO AL METODO PRINCIPAL..."
        return 1
    else:
        print "¬(z >= 0)"
        print "retornando z = 0"
        print "-------"
        print "VOLVIENDO AL METODO PRINCIPAL..."
        return 0

def entrenar_perceptron(datos_ent, pesos, t, l):
        print "ENTRENAMIENTO DEL PERCEPTRON"
        errores=True
        print "RECIBIENDO DATOS Y AJUSTANDO PESOS"
        while errores:
            errores=False

## entrenar perceptron
            
            for k,y in datos_ent.iteritems():
                print "ITERACION SOBRE LA TABLA DE DATOS"
                z = salida(k, pesos, t)
                print "CHEQUEO SI z ES DISTINTO DE y"
                if z!=y:
                    print "(!) z!=y"
                    print "y="+str(y)
                    print "z="+str(z)
                    errores=True
                    e=(y-z)
                    print "CALCULANDO ERROR"
                    print "e=(y-z)="+str(e)
                    delta_t=-(l*e)
                    print "CALCULANDO DELTA THETA"
                    print "delta_t=-(l*e)="+str(delta_t)
                    t=t+delta_t
                    print "CALCULANDO NUEVO VALOR DE THETA"
                    print "t=t+delta_t="+str(t)
                    print "CALCULANDO PESOS FINALES"
                    for i in range(len(k)):
                        delta_w=l*e*k[i]
                        print "DELTA W"+str(i)+"=l*e*k["+str(i)+"]="+str(delta_w)
                        pesos[i]=pesos[i]+delta_w
                        print "PESOS["+str(i)+"]=pesos["+str(i)+"]+delta_w="+str(pesos[i])
                else:
                    print "(!) z=y"
        return pesos, t

def clasificar(entrada, pesos, t):
    return salida(entrada, pesos, t)

if __name__ == "__main__":
    
    datos_ent = {(0, 0):0, (0,1):1, (1,0):1, (1,1):1}
    pesos=[0.2, -0.5]
    t=0.4
    l=0.2
    pesos, t = entrenar_perceptron(datos_ent, pesos, t, l)
    print clasificar((0,1), pesos, t)

    
