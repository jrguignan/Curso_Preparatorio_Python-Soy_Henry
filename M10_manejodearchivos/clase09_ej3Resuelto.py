montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}


listaclaves = list(montañas.keys())
listavalores = list(montañas.values())

Datos = open('clase09_ej3Resuelto.csv', 'w')
linea = listaclaves[0]
for i in range(1,len(listaclaves)):
    linea = linea + ',' +  str(listaclaves[i])
    if i == 4:
        Datos.write(linea+'\n')
        

for l in range(0,len(listavalores[0])):
    linea = str(listavalores[0][l])
    for i in range(1,len(listaclaves)):
        Datos = open('clase09_ej3Resuelto.csv', 'a')
        linea = linea + ',' +  str(listavalores[i][l])
        if i == 4:
           Datos.write(linea+'\n')  

Datos.close()  