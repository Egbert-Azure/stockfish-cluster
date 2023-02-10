
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
$ mpirun -np 2 --host mycluster1,mycluster2 ./osu-micro-benchmarks-6.1/install/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency
```
This will run the latency test between nodes 1 and 2 (mycluster1 and mycluster2) on your 4 node Azure cluster.

It is important to document your results and the configuration of your cluster for future reference. These benchmarks can also be useful when tuning and optimizing your cluster for specific workloads.
