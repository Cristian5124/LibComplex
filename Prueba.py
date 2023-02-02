import Libcomplex as cplx

passed =0
failed =0

#Prueba 1 (Suma de complejos)
c1=(3,-8)
c2=(4,6)
resp=cplx.sumacomplex(c1,c2)
 
if resp[0]==7 and resp[1]==-2:
    passed += 1
else:
    failed+=1

#Prueba 2 (Producto entre complejos)
c1=(2,-3)
c2=(-1,1)
resp=cplx.multcomplex(c1,c2)
 
if resp[0]==1 and resp[1]==5:
    passed += 1
else:
    failed+=1

#Prueba 3 (Resta de complejos)
c1=(1,-1)
c2=(-2,-5)
resp=cplx.restacomplex(c1,c2)
 
if resp[0]==3 and resp[1]==4:
    passed += 1
else:
    failed+=1

#Prueba 4 (División entre complejos)
c1=(3,2)
c2=(-1,2)
resp=cplx.divcomplex(c1,c2)
 
if resp[0]==1 and resp[1]==-8 and resp[2]==5:
    passed += 1
else:
    failed+=1

#Prueba 5 (Modulo de un complejo)
c=(-2,-3)
resp=cplx.modulocomplex(c)
 
if resp==3.605551:
    passed += 1
else:
    failed+=1

#Prueba 6 (Conjugado de un complejo)
c=(7,-4)
resp=cplx.conjugadocomplex(c)
 
if resp[0]==7 and resp[1]==4:
    passed += 1
else:
    failed+=1

#Prueba 7 (Fase o argumento de un complejo)
c=(7,-4)
resp=cplx.fasecomplex(c)
 
if resp==-29.744881:
    passed += 1
else:
    failed+=1

#Prueba 8 (Representación cartesiana a polar)
c=(7,-4)
resp=cplx.polarcomplex(c)
 
if resp[0]==8.062258 and resp[1]==-29.744881:
    passed += 1
else:
    failed+=1

#Impresión de los resultados de las pruebas
print("Passed: ",passed," | Failed: ",failed)