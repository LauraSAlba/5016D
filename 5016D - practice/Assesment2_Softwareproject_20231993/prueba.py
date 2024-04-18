from os import system
import pandas as pd
from datetime import datetime

system("clear")
print("=====BIENVENIDO=====\n\n\t\t\t[SISTEMA DE TICKETS]\n\n")

opcion = str(input("estimado Usuario, por favor seleccione la opcion deseada:\n\n1. Generar Ticket \n"
                   " 2. Consultar Ticket \n 3. Salir\n\n================\n\nSu opcion es:"))



def ticket():
    file = 'CatalogoCategoria.csv'
    categoria = pd.read_csv(file, nrows=100)

    print("\t\tSISTEMA DE TICKETS\n\nClave\tcategoria\n==========")
    for i in range(len(categoria)):
        for j in range(len(categoria.iloc[i])):
            print(categoria.iloc[i][j], end='\t\t')
            print()

    opcion = str(input
                 ("=========\nCapture la Calve de la Categoria :"))
    desc = str(input("Descripcion breve del problema:"))

    i = 0
    repetir_bucle = True
    while repetir_bucle:
        repetir_bucle = (opcion != categoria.iloc[i][0])
        nom_categoria = str(categoria.iloc[i][1])
        i = i + 1
        print(f"\nLa Categoris Selecionada es{nom_categoria}\nDescripcion: {desc}")

        def cat_empleado():
            file = 'CatalogoEmpleado.csv'
            empleado = pd.read_csv(file, nrows=100)
            numero = int(input("\nCapture numero de empleado:"))
            system("clear")

            e = 0
            repetir_bucle = True
            while repetir_bucle:
                repetir_bucle = (empleado.iloc[e][0] != numero)
                nombre = str(empleado.iloc[e][1])
                area = str(empleado.iloc[e][2])
                mihora = datetime.now()
                e = e + 1
                print(f"\nEstimada/o: {nombre}\nDepatamento{area}\nSe ha generado su ticket con la fecha y"
                      f"hora:\n{mihora}\n\n. En breve su solicitud sera arendida . ")

                nticket = str(input("\nDesea realizar otro reporte s/n : "))

                if (nticket == "s"):
                    ticket()
                    cat_empleado()
                if (nticket == "n"):
                    print("Muchas gracias, hasta luego 0")

                def consultas():
                    file = 'historico.csv'
                    consul = pd.read_csv(file, nrows=100)
                    opcion = str(input("\nCapture el numero del reporte: "))

                    i = 0
                    repetir_bucle = True
                    while repetir_bucle:
                        repetir_bucle = (consul.iloc[i][0] != opcion)
                        usuario = str(consul.iloc[i][1])
                        estatus = str(consul.iloc[i][3])
                        i = i + 1
                        print(f"\nEstimado/a: {usuario}\n Tu ticket"
                              f"{opcion}\n tiene estatus: {estatus}")

                        cticket = str(input("\nDesea consultar otro reporte s/n : "))
                        system("clear")
                        if (cticket == "s"):
                            consultas()
                        if (cticket == "n"):
                            print("Muchas gracias, hasta luego")

                        if (opcion == "1"):
                            ticket()
                            cat_empleado()
                        elif (opcion == "2"):
                            consultas()
                        elif (opcion == "3"):
                            print("Gracias, hasta luego")
                        else:
                            print("la opcion no existe.")
