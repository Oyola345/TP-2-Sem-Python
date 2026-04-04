rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7,
                          'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8,
                      'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9,
                       'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7,
                         'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
                      'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9,
                          'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7,
                      'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6,
                       'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8,
                         'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8,
                      'judge_3': 7},
        }
    },
    {
        'theme': 'Postre', 'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8,
                          'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9,
                      'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7,
                       'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7,
                         'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9,
                      'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9,
                          'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6,
                      'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8,
                       'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9,
                         'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7,
                      'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8,
                          'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9,
                      'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7,
                       'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9,
                         'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8,
                      'judge_3': 7},
        }
    }
]

# Imprima la tabla de posiciones luego de cada ronda para ver la progresión de
# la competencia. Cada ronda debe indicar quién fue el ganador (mayor puntaje en la ronda).
# La cantidad de rondas ganadas se debe contabilizar.
# Se debe imprimir la tabla final con: puntaje total acumulado, cantidad de
# rondas ganadas, mejor puntaje en una ronda, y promedio por ronda. La tabla
# debe estar en orden decreciente por puntaje total

pos_final = {}

nro_round = 0
for round in rounds:
    nro_round += 1
    posiciones = []

    for participante in round['scores']:
        posiciones.append(
            {'Nombre': participante,
             'Puntaje': sum(round['scores'][participante].values())})

        if (nro_round == 1):
            pos_final.update(
                {participante: {'Acumulado': posiciones[-1]['Puntaje'], 'Victorias': 0, 'Mejor puntaje': posiciones[-1]['Puntaje'], 'Promedio': posiciones[-1]['Puntaje']}})
        else:
            pos_final[participante]['Acumulado'] += posiciones[-1]['Puntaje']

            if (posiciones[-1]['Puntaje'] > pos_final[participante]['Mejor puntaje']):
                pos_final[participante]['Mejor puntaje'] = posiciones[-1]['Puntaje']

            pos_final[participante]['Promedio'] = pos_final[participante]['Acumulado']/nro_round

    posiciones = sorted(
        posiciones, key=lambda item: item['Puntaje'], reverse=True)

    pos_final[posiciones[0]['Nombre']]['Victorias'] += 1

    print(f"\nRonda {nro_round} - {round['theme']}:")
    print(
        f"  *Ganador: {posiciones[0]['Nombre']} ({posiciones[0]['Puntaje']} puntos)")

    nro_puesto = 1
    for puesto in posiciones[1:]:
        nro_puesto += 1
        print(
            f"  Puesto {nro_puesto}: {puesto['Nombre']} ({puesto['Puntaje']} puntos)")

print()
pos_final = dict(sorted(pos_final.items(), key=lambda item: item[1]['Acumulado'], reverse=True))

ancho_nom = 13 
ancho_num = 18
ancho_vic = 23

print("Tabla de posiciones final:")
print(f"{'Cocinero':<{ancho_nom}}"
      f"{'Puntaje':>{ancho_num}}"
      f"{'Rondas ganadas':>{ancho_vic}}"
      f"{'Mejor ronda':>{ancho_num}}"
      f"{'Promedio':>{ancho_nom}}")

print("-" * (ancho_nom + ancho_num * 4))

for chef in pos_final:
    datos = pos_final[chef]
    print(f"{chef:<{ancho_nom}}"
          f"{datos['Acumulado']:>{ancho_num}}"
          f"{datos['Victorias']:>{ancho_num}}"
          f"{datos['Mejor puntaje']:>{ancho_num}}"
          f"{datos['Promedio']:>{ancho_num}}")