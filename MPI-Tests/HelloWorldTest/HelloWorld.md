# Hello World Test

Here we have a basic MPI hello world application to test our cluster. 
> **Note** - All of the code for this site is on [GitHub]({{ site.github.repo }}). This tutorial's code is under [tutorials/mpi-hello-world/code]({{ site.github.code }}/tutorials/mpi-hello-world/code).

## Hello world code examples
Let's do a first test with a Hello World example


```cpp
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    // Initialize the MPI environment
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Get the rank of the process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Get the name of the processor
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    // Print off a hello world message
    printf("Hello world from processor %s, rank %d out of %d processors\n",
           processor_name, world_rank, world_size);

    // Finalize the MPI environment.
    MPI_Finalize();
}
```

## Compiling the MPI hello world application
All parallel computing software needs to be compiled with mpicc. Let's create an executable file:
```console
mpicc -o mpi_hello_world mpi_hello_world.c
```
After your program is compiled, it is ready to be executed. Now comes the part where you might have to do some additional configuration. If you are running MPI programs on a cluster of nodes, you will have to set up a host file. If you are simply running MPI on a laptop or a single machine, disregard the next piece of information.

The host file contains names of all of the computers on which your MPI job will execute. For ease of execution, you should be sure that all of these computers have SSH access, to avoid a password prompt for SSH. My host is named *chessbase * and looks like this.

```
>>> cat chessbase
#STOCKFISH CLUSTER
# ClusterManager
10.0.0.100 
# ClusterNode1
10.0.0.101
# ClusterNode2
10.0.0.102 
# ClusterNode3
10.0.0.103 
```
running the programm with mpirun on cust ClusterMaster:
```
mpirun ./helloworld

Hello world from processor ClusterMaster, rank 3 out of 4 processors
Hello world from processor ClusterMaster, rank 0 out of 4 processors
Hello world from processor ClusterMaster, rank 1 out of 4 processors
Hello world from processor ClusterMaster, rank 2 out of 4 processors
```
and now the same on all nodes and the master using the hostfile:
```console
mpirun --hostfile ./chessbase ./helloworld

Hello world from processor ClusterMaster, rank 1 out of 16 processors
Hello world from processor ClusterMaster, rank 3 out of 16 processors
Hello world from processor ClusterMaster, rank 0 out of 16 processors
Hello world from processor ClusterMaster, rank 2 out of 16 processors
Hello world from processor ClusterNode2, rank 9 out of 16 processors
Hello world from processor ClusterNode1, rank 6 out of 16 processors
Hello world from processor ClusterNode2, rank 11 out of 16 processors
Hello world from processor ClusterNode1, rank 7 out of 16 processors
Hello world from processor ClusterNode3, rank 14 out of 16 processors
Hello world from processor ClusterNode2, rank 8 out of 16 processors
Hello world from processor ClusterNode1, rank 4 out of 16 processors
Hello world from processor ClusterNode3, rank 15 out of 16 processors
Hello world from processor ClusterNode2, rank 10 out of 16 processors
Hello world from processor ClusterNode1, rank 5 out of 16 processors
Hello world from processor ClusterNode3, rank 12 out of 16 processors
Hello world from processor ClusterNode3, rank 13 out of 16 processors
```

As expected, the MPI program was launched across all of the hosts in my host file. Each process was assigned a unique rank, which was printed off along with the process name. As one can see from my example output, the output of the processes is in an arbitrary order since there is no synchronization involved before printing.

Now you might be asking, *"My hosts are actually dual-core machines. How can I get MPI to spawn processes across the individual cores first before individual machines?"* The solution is pretty simple. Just modify your hosts file and place a colon and the number of cores per processor after the host name. For example, I specified that each of my hosts has just 2 cores and ClusterMaster is first to use.

```
>>> cat chessbase
#STOCKFISH CLUSTER
# ClusterManager
10.0.0.100 slots=2 
# ClusterNode1
10.0.0.101 slots=2
# ClusterNode2
10.0.0.102 slots=2
# ClusterNode3
10.0.0.103 slots=2
```
Executinge the run script again, *voila!*, the MPI job spawns just 2 processes on only two of my hosts.
```
mpirun --hostfile ./hosttest ./helloworld

Hello world from processor ClusterMaster, rank 0 out of 8 processors
Hello world from processor ClusterMaster, rank 1 out of 8 processors
Hello world from processor ClusterNode2, rank 4 out of 8 processors
Hello world from processor ClusterNode2, rank 5 out of 8 processors
Hello world from processor ClusterNode1, rank 2 out of 8 processors
Hello world from processor ClusterNode3, rank 6 out of 8 processors
Hello world from processor ClusterNode3, rank 7 out of 8 processors
Hello world from processor ClusterNode1, rank 3 out of 8 processorss
```
