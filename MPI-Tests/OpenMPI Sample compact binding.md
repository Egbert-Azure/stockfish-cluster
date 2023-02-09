# OpenMPI Sample Program
## Multithreading with OpenMP and KMP_AFFINITY

Demonstrate how to run an OpenMP program using OpenMPI and the compact binding strategy.

## Program Code
``` c
#include <mpi.h>
#include <omp.h>
#include <iostream>

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);

    // Set the KMP_AFFINITY environment variable to "compact"
    setenv("KMP_AFFINITY", "compact", 1);

    // Get the number of available threads
    int nthreads = omp_get_num_threads();
    std::cout << "Number of threads: " << nthreads << std::endl;

    // Parallel section
    #pragma omp parallel
    {
        // Get the thread ID
        int id = omp_get_thread_num();
        std::cout << "Hello from thread " << id << std::endl;
    }

    MPI_Finalize();
    return 0;
}
```
## Compiling and Running the Program

To compile the program, use the following command:
``` s
$ mpic++ -fopenmp openmpi_sample.cpp -o openmpi_sample
```
To run the program using the compact binding strategy, use the following command:
``` s
$ mpirun -np [number of processes] -x KMP_AFFINITY=compact openmpi_sample
```
