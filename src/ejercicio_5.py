# Calcule el costo de envío de un paquete según su peso (en kg) y la zona de
# destino. El usuario debe ingresar ambos valores.
# Las zonas válidas son: local, regional, nacional.
# Peso / Zona       local regional nacional
# Hasta 1 kg        $500    $1000   $2000
# Entre 1 y 5 kg    $1000   $2500   $4500
# Más de 5 kg       $2000   $5000   $8000

# Si la zona no es válida, debe indicar el error

def categorizar_peso(peso):
    if (peso < 1):
        return "Bajo"
    else:
        if (1 <= peso <= 5):
            return "Medio"
        else:
            return "Alto"


precios = {
    "Bajo": {
        "local": 500,
        "regional": 1000,
        "nacional": 2000},
    "Medio": {
        "local": 1000,
        "regional": 2500,
        "nacional": 4500
    },
    "Alto": {
        "local": 2000,
        "regional": 5000,
        "nacional": 8000
    }
}

peso = float(input("Ingrese el peso del paquete (kg): "))

while True:
    zona = input("Ingrese la zona de destino (local/regional/nacional): ")
    match zona:
        case "local" | "regional" | "nacional":
            costo = precios[categorizar_peso(peso)][zona]
            break
        case _:
            print("Zona no válida. Las zonas disponibles son: local, regional, nacional.")

print(f"Costo de envío: {costo}")
