# OpenMPI Sample Program
## Multithreading with OpenMPI and KMP_AFFINITY on Linux

Multithreading is a technique to parallelize a program and execute multiple threads simultaneously in order to optimize performance. In HPC (High Performance Computing) environments, this is particularly important for large-scale simulations and data processing tasks. OpenMPI is a widely-used MPI (Message Passing Interface) library for parallel computing that supports multithreading. In addition to that, OpenMPI allows the use of the KMP_AFFINITY environment variable to specify the binding preferences for threads, which is particularly useful for multithreaded programs.
Setting KMP_AFFINITY with OpenMPI
OpenMPI supports multithreading through the use of the KMP_AFFINITY environment variable. This variable has three principal binding strategies:

- compact: fills up one socket before allocating to other sockets
- scatter: evenly spreads threads across all sockets and cores
- explicit: allows you to define exactly which cores/sockets to use

## Program Code
``` c
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    printf("Hello from rank %d of %d\n", rank, size);

    MPI_Finalize();
    return 0;
}
```
The `MPI_Init` function initializes the MPI environment, and `MPI_Comm_rank` and `MPI_Comm_size` are used to obtain the rank and size of the MPI process, respectively. The program simply prints a message indicating the rank and size of the process.

To compile and run the program with OpenMPI and KMP_AFFINITY, you would use the following commands:

``` s
mpicc -o openmpi_KMP_AFFINITY openmpi_KMP_AFFINITY.c
export KMP_AFFINITY=compact
mpirun -np 4 openmpi_KMP_AFFINITY
```
 `mpicc` is used to compile the program, and mpirun is used to run the program with 4 processes. The -np option is used to specify the number of processes. The export command is used to set the KMP_AFFINITY environment variable to compact, which means that the threads will be preferentially bound to a single socket before being bound to other sockets.
