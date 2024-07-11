#Práctica 8: Cómputo Paralelo en un Cluster con Linux
#------------------------------------------------------
# Instalacion Pillow Linux => Debian 10 para procesar imagenes en el cluster linux
#sudo apt update
#sudo apt install python3-pip
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
#------------------------------------------------------

#Horas
from datetime import datetime, date, time, timedelta
#Imagenes
from PIL import Image

#MPI
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank

if rank==0:
    #Pedir imagen
    nombreImagen = input('Nombre y extencion de la imagen: ')

    #Hora de inicio
    inicio = datetime.now()
    print('Hora de inicio => '+ str(inicio.strftime("%H:%M:%S")))
    
    #Procesamiento de la imagen
    print('Leyendo la imagen ...')
    imagen = Image.open(nombreImagen)
    pixelesRGB = list(imagen.getdata())
    
    #Separara la imagen y enviarla al otro nodo
    print('Enviando datos al esclavo ...')
    mitadPixeles = [pixelesRGB[x] for x in range(int(len(pixelesRGB)/2)+1, len(pixelesRGB))]
    comm.send(mitadPixeles, dest=1)

    #Conversion a escala de grises y resive la otra mitad del nodo
    print('Procesando Maestro ...')
    pixelesBN1 = [round((0.2125 * pixelesRGB[x][0]) + (0.7154 * pixelesRGB[x][1]) + (0.072 * pixelesRGB[x][2])) for x in range(0, int(len(pixelesRGB)/2))]
    print('Resiviendo datos del esclavo ...')  
    pixelesBN2=comm.recv(source=1)

    #Nueva imagen
    print('Procesando nueva imagen ...')
    imagenGris = Image.new('L', imagen.size)
    imagenGris.putdata(pixelesBN1 + pixelesBN2)
    imagenGris.save('Escala-grises.png')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('GUARDO LA IMAGEN '+nombreImagen+' EN ESCALA DE GRISES EN LA NUEVA IMAGEN LLAMADA Escala-grises.png')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    #Hora de fin
    fin = datetime.now()
    print('Hora de fin => '+ str(fin.strftime("%H:%M:%S")))

    #Tiempo de ejecucion
    print('Tiempo de procesamiento => '+str(fin-inicio))
if rank==1:
    #Resivir el nombre de la imagen
    mitadPixeles = comm.recv(source=0)
    print('Resiviendo datos esclavo ...')
    
    #Procesar los pixeles y enviarlos al maestro
    print('Procesando Esclavo ...')
    pixelesBN = [round((0.2125 * mitadPixeles[x][0]) + (0.7154 * mitadPixeles[x][1]) + (0.072 * mitadPixeles[x][2])) for x in range(len(mitadPixeles))]
    
    #Enviar pixeles al nodo maestro
    print('Enviando datos procesados a Maestro ...')
    comm.send(pixelesBN, dest=0)