print ('que onda muchachos')

txt = input ("Ingrese el archivo para analizar: ")
try :
    handle = open (txt)
except:
    print("Se ha ingresado un archivo no valido")
    quit()

#Genero el diccionario con palabras y numero de repeticion
count = dict()
for lines in handle :
    lines = lines.rstrip() #Las lineas es un str entero con varias palabras
    words = lines.split()  #words es un list con las distintas palabras del str    
    for word in words:
        count[word] = count.get(word,0) + 1

#Creo un tuple de núm de repeticion(value) y palabras(keys), para ordenarlos de mayor a menor
lst = list()
for (k,v) in count.items():
    lst.append( (v,k) )
lst = sorted(lst, reverse= True)

print ("Las 10 palabras mas repetidas son:")    
for (v,k) in lst[:10]:
    print (k,v)


