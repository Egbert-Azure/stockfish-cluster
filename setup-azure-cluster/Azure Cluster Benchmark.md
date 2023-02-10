
# Azure Cluster Benchmark
If you want to do some basic performance testing, try the OSU Micro-Benchmarks. First, install the dependencies necessary to build the benchmarks:
``` console
$ sudo apt-get -y update
$ sudo apt-get -y install make g++
```
Next, download and extract the OSU Micro-Benchmarks package:
``` console
$ wget https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-6.1.tar.gz
$ tar zxf osu-micro-benchmarks-6.1.tar.gz
$ cd osu-micro-benchmarks-6.1/
```
Configure the build using MPI compilers:
``` console
$ ./configure --prefix $PWD/install CC=mpicc CXX=mpicxx
$ make && make install
```
Copy the compiled app to all nodes in your cluster:
``` 
$ cd
$ clush -w mycluster[1-3] -c osu-micro-benchmarks-6.1
```
To run the latency test, use the mpirun command, specifying the number of processes with the -np option, and the host nodes with the --host option:
```
$ mpirun -np 2 --host mycluster1,mycluster2 ./osu-micro-benchmarks-6.1/install/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency > latency_results.txt
```
This will run the latency test between nodes 1 and 2 (mycluster1 and mycluster2) on your 4 node Azure cluster and store the results of the latency test into the file latency_results.txt.

The numbers in the results tell you the performance of the MPI communication between the two nodes. In the case of the latency test, the results show the time it takes for a message to be sent from one node to another and for a response to be received, in microseconds. The results include the minimum, maximum, average, and standard deviation of the latency for a specified number of message exchanges between the nodes.

It's important to note that the results of the OSU Micro-Benchmarks are not absolute measures of performance, but rather relative measures. The results can be used as a comparison between different configurations or to track changes in performance over time. It's also important to keep in mind that the performance of an MPI communication depends on many factors, including the network, hardware, and MPI implementation.
