import json
import sys
import os
import subprocess
import pyfiglet

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_texto_en_json(archivo_json, texto_buscar):
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)

        resultados = []
        for item in data:
            if texto_buscar in item.get('kernel_name', ''):
                resultados.append(item)

        return resultados
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_json} no fue encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Error: El archivo {archivo_json} no es un JSON válido.")
        return []

def leer_kernels_de_archivo(archivo_kernels):
    try:
        with open(archivo_kernels, 'r') as f:
            kernels = [linea.strip() for linea in f.readlines() if linea.strip()]
        return kernels
    except FileNotFoundError:
        print(f"Error: El archivo {archivo_kernels} no fue encontrado.")
        return []

def mostrar_ayuda():
    ayuda = """
Uso: python3 kernel_finder.py -k <kernel> | -f <archivo_kernels>

Opciones:
  -k <kernel>               Especifica un único kernel para buscar.
  -f <archivo_kernels>      Especifica el archivo que contiene la lista de kernels a buscar.
  -h                        Muestra este mensaje de ayuda.
"""
    print(ayuda)

def validar_archivo_json(archivo_json):
    if not os.path.exists(archivo_json):
        print(f"Kernel database not found\n")
        subprocess.run(['python3', 'data/kernel_scraper.py', '-o', archivo_json])

def main():
    limpiar_pantalla()

    banner = pyfiglet.figlet_format("KPF")
    print(banner)
    print(Kernel-debug Packet Finder)

    archivo_json = 'kernel_list.json'
    validar_archivo_json(archivo_json)

    if len(sys.argv) != 2 and sys.argv[1] == '-h':
        mostrar_ayuda()
        return

    if len(sys.argv) == 3 and sys.argv[1] == '-k':
        kernel_unico = sys.argv[2]
        resultados = buscar_texto_en_json(archivo_json, kernel_unico)

        if resultados:
            distribuciones = set(item['distribucion'] for item in resultados)

            for distribucion in distribuciones:
                print(f"Searching kernel: {kernel_unico}\n")
                print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                print("|              | Detail                                                                                                                 ")
                print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                for resultado in resultados:
                    if resultado['distribucion'] == distribucion:
                        print(f"| Distribution | {resultado['distribucion']:<109} ")
                        print(f"| Kernel Name  | {resultado['kernel_name']:<109} ")
                        print(f"| URL          | {resultado['url']:<109} ")
                        print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
        else:
            print(f"Searching kernel: {kernel_unico}\n")
            print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
            print("|              | Detail                                                                                                                 ")
            print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
            print(f"| Distribución | Not found")
            print(f"| Kernel Name  | Not found")
            print(f"| URL          | Not found")
            print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")

    elif len(sys.argv) == 3 and sys.argv[1] == '-f':
        archivo_kernels = sys.argv[2]
        kernels_a_buscar = leer_kernels_de_archivo(archivo_kernels)

        if not kernels_a_buscar:
            print("Error: El archivo no contiene ningún kernel.")
            return

        for kernel in kernels_a_buscar:
            print(f"\nSearching kernel: {kernel}")
            resultados = buscar_texto_en_json(archivo_json, kernel)

            if resultados:
                distribuciones = set(item['distribucion'] for item in resultados)

                for distribucion in distribuciones:
                    print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                    print("|              | Detail                                                                                                                 ")
                    print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                    for resultado in resultados:
                        if resultado['distribucion'] == distribucion:
                            print(f"| Distribución | {resultado['distribucion']:<109} ")
                            print(f"| Kernel Name  | {resultado['kernel_name']:<109} ")
                            print(f"| URL          | {resultado['url']:<109} ")
                            print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
            else:
                print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                print("|              | Detail                                                                                                                 ")
                print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")
                print(f"| Distribución | Not found")
                print(f"| Kernel Name  | Not found")
                print(f"| URL          | Not found")
                print("+--------------+----------------------------------------------------------------------------------------------------------------------- ")

    else:
        print("Uso: python3 kernel_finder.py -k <kernel> | -f <archivo_kernels>")

if __name__ == '__main__':
    main()
