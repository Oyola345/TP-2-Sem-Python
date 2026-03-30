text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

total_lineas = len(text.splitlines())
total_palabras = len(text.split())
print(f"Total de líneas: {total_lineas}")
print(f"Total de palabras: {total_palabras}")
promedio = total_palabras/total_lineas
print(f"Promedio de palabras por línea: {promedio:.2f}")

print(f"Líneas por encima del promedio ({promedio:.2f} palabras):")
lineas = text.splitlines()
for linea in lineas:
    cant = len(linea.split())
    if cant > promedio:
        print(f'- "{linea}" ({cant} palabras)')
