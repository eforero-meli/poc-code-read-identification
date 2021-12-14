import zxing
import re
# from operator import itemgetter
import numpy as np

reader = zxing.BarCodeReader()

# barcode = reader.decode('document_01.png')
barcode = reader.decode('document_02.jpeg')

arraySplit = barcode.raw.split('\x00')
# print('Barcode Total:', arr)

arraySeparteByNumbersAndLetters = list(map(lambda value: re.split('(\d+)',value), arraySplit))
onlyArray = list(np.concatenate(arraySeparteByNumbersAndLetters).flat)
arrayClean = list(filter(lambda value: value != '', onlyArray))

carry=False
if arrayClean[7].isnumeric():
    carry=True 

# arrIndexWithData = [3,4,5,6,7,8,9,10,11]
# arrData = itemgetter(*arrIndexWithData)(arrayClean)
# print('ArrayData:', arrData)

def getIdNumber():
    return arrayClean[3][-10:]

def getFirstSurname():
    return arrayClean[4]

def getSecondSurname():
    return arrayClean[5]

def getFirstName():
    return arrayClean[6]

def getSecondName():
    if carry:
        return
    return arrayClean[7]

def getGender():
    if carry:
        return arrayClean[8]
    return arrayClean[9]

def getBirthDate():
    if carry:
        return arrayClean[9][0:8]
    return arrayClean[10][0:8]

def getBloodType():
    if carry:
        return arrayClean[10]
    return arrayClean[11]

print('Cédula de ciudadania:', getIdNumber())
print('Primer Apellido:', getFirstSurname())
print('Segundo Apellido:', getSecondSurname())
print('Primer Nombre:', getFirstName())
print('Segundo Nombre:', getSecondName())
print('Genero:', getGender())
print('Fecha de nacimiento:', getBirthDate())
print('Tipo de sangre:', getBloodType())
# print('Información procesada:',  arrayClean)
