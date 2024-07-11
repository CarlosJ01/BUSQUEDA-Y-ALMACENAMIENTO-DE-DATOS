# mpiexec -n 2 --hosts ip1,ip2 pyhton hola_mundo.py
from mpi4py import MPI
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
print("\nHola Mundo con MPI")
print("El tamaño del Cluster es: " + str(size))
print("Mi rango es: " + str(rank))
print("Mi nombre es: " + str(name))