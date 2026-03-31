playlist = [
    {"title": "Bohemian Rhapsody", "duration": "5:55"},
    {"title": "Hotel California", "duration": "6:30"},
    {"title": "Stairway to Heaven", "duration": "8:02"},
    {"title": "Imagine", "duration": "3:07"},
    {"title": "Smells Like Teen Spirit", "duration": "5:01"},
    {"title": "Billie Jean", "duration": "4:54"},
    {"title": "Hey Jude", "duration": "7:11"},
    {"title": "Like a Rolling Stone", "duration": "6:13"},
]

total_mins = 0
total_segs = 0
min = 1000
max = 0

for cancion in playlist:
    tiempo = cancion["duration"].split(":")

    mins = int(tiempo[0])
    total_mins += mins

    segs = int(tiempo[1])
    total_segs += segs

    segs += mins*60
    if segs > max:
        max = segs
        cancion_max = cancion["title"]
        duracion_max = cancion["duration"]
    else:
        if segs < min:
            min = segs
            cancion_min = cancion["title"]
            duracion_min = cancion["duration"]

if (total_segs > 60):
    num = total_segs // 60
    total_segs = total_segs - num*60
    total_mins += num

print(f"Duración total: {total_mins}m {total_segs}s")
print(f'Canción más larga: "{cancion_max}" ({duracion_max})')
print(f'Canción más corta: "{cancion_min}" ({duracion_min})')
