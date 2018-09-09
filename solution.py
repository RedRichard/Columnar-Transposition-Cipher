from math import ceil

def cryptographer(oText, key):
    sectionsOrd = []
    seenLetter = None

    #Preparación de la cadena:
    oText = oText.strip().replace(" ","")

    #Añadido de caracteres extras al final:
    auxC = (len(oText)/len(key))
    oText += oText[-1]*int(float("%.1f" %((ceil(auxC)-auxC)*len(key))))

    #Proceso:
    sectionsV = [oText[i::len(key)] for i in range(len(key))]
   
    for letter in sorted(key):
        if letter == seenLetter:
            auxIndex = key.find(letter, auxIndex+1)
        else:
            auxIndex = key.find(letter)
        seenLetter = letter
        sectionsOrd.append(sectionsV[auxIndex])

    return ''.join(sectionsOrd)

def decipher(cText, key):
    sectionsOrd, seenLetters = [],[]

    auxCount = int(len(cText)/len(key))
    sectionsV = [cText[i:i+auxCount] for i in range(0, len(cText), auxCount)] 
    
    for letter in key:
        auxIndex = ''.join(sorted(key)).find(letter)
        while auxIndex in seenLetters:
            auxIndex+=1
        seenLetters.append(auxIndex)
        sectionsOrd.append(sectionsV[auxIndex])
        
    strOrd = ''.join(sectionsOrd)
    res = [strOrd[i::auxCount] for i in range(auxCount)]
    return ''.join(res)

print(cryptographer("LA CRIPTOGRAFIA ES ROMANTICA", "HALAJA"))
print(decipher("AOAAARRSTAPFOCALTIMAIARIACGENA", "HALAJA"))

print(cryptographer("LA CRIPTOGRAFIA ES ROMANTICA", "HOLA"))
print(decipher("ROFSACALIGIRNACTAEMIAAPRAOTA","HOLA"))

print(cryptographer("HOLA TU", "YOO"))
print(decipher("OTLUHA","YOO"))

print(cryptographer("DEFEND THE EAST WALL OF THE CASTLE", "GERMAN"))
print(decipher("NALCEEHWTTDTTFSEELEEDSOAEFEAHL","GERMAN"))
