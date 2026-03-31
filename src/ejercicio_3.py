review = """La película sigue a un grupo de astronautas que viajan a Marte en una misión de rescate. El capitán Torres lidera al equipo a través de tormentas solares y fallos en el sistema de navegación. Al llegar a Marte descubren que la base está abandonada y los suministros destruidos. Torres decide sacrificar la nave nodriza para salvar al equipo y logran volver a la Tierra en una cápsula de emergencia.
El final revela que Torres sobrevivió gracias a un pasaje secreto."""

spoilers = input(
    "Ingrese las palabras spoiler (separadas por coma): ")
palabras = spoilers.split(",")
palabras = [n.strip().lower() for n in palabras]

list_review = review.split()
pos = 0
for palabra in list_review:
    if palabra.lower() in palabras:
        list_review[pos] = len(palabra) * "*"
    pos += 1

review = " ".join(list_review)
print(review)
