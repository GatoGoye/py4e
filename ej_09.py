print ('que onda muchachos')

txt = input ("Ingrese el archivo para analizar: ")
handle = open (txt)

count = dict()
for lines in handle :
    lines = lines.rstrip()
    # print(lines)
    words = lines.split()
    # print (words)
    for word in words:
        count[word] = count.get(word,0) + 1

# print(count)

Word_Rep = None
Num_Rep = None

for word,count in count.items():    
    if Num_Rep == None or Num_Rep < count :    
        Word_Rep = word
        Num_Rep = count


print ('La Palabra mas repetida es:',Word_Rep, "escrita",Num_Rep, "veces")


