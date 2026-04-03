posts = ["Arrancando el lunes con energía #Motivación #NuevaSemana",
         "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
         "No puedo creer el final de la serie #SinSpoilers #SerieAdicta", "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
         "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
         "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
         "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
         "Finde de lluvia, maratón de series #SerieAdicta #Relax",
         "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
         ]

hashtags = {}
palabras = []

for post in posts:
    palabras.extend(post.split())

for palabra in palabras:
    if "#" in palabra:
        if palabra not in hashtags:
            hashtags.update({palabra: palabras.count(palabra)})

hashtags = dict(sorted(hashtags.items(), key=lambda item: item[1], reverse=True))

trends = [hashtag for hashtag in hashtags if hashtags[hashtag] > 1]

print("\nHashtags trending (más de una aparición): ")
for trend in trends:
    print(f"{trend}: {hashtags[trend]}")

print(f"\nTotal de hashtags únicos: {len(hashtags)}")
