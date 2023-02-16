# Install the Stockfish Cluster Engine

Now that you have your cluster up and running on either a single board computer or on Azure, it's time to move onto the installation of the cluster version of the Stockfish chess engine. This version uses parallel computing with OpenMPI to connect processes running on multiple computers and allow them to communicate with each other as they run. This allows you to run a single script across multiple cluster nodes.

## Dependencies

- openmpi-bin
- openmpi-common
- libopenmpi3
- libopenmpi-dev

First, you'll need to clone the Stockfish Cluster branch:

We only need to clone the Stockfish Cluster branch:

``` clone
git clone --branch cluster --single-branch https://github.com/official-stockfish/Stockfish.git cluster
```

Next step is to compile the cluster version with the make file.

To optimze the implementation, check out the processor of all nodes to use the right ARCH paramenter. As an example, you can determine the processor running on your Standard DS1 v2 Azure virtual machine by using the `lscpu` command. Result might be Intel(R) Xeon(R) Platinum 8171M CPU @ 2.60GHz. In that case, your nodes are running on Intel Xeon Platinum 8171M (Skylake) processors. You might be able to use the following ARCH value (at least `ARCH=x86-64-modern`)

``` consol
cd cluster/src
$ make build ARCH=x86-64-modern-Skylake COMPILER=mpicxx
```

>Note: The ARCH flag can be set to a variety of different architectures, depending on your setup. The COMPILER=mpicxx syntax specifies that you want to use the MPI compiler

``` console
 sudo cp /home/`user`/cluster/src/stockfish /usr/games/stockfish15

 clush -w mycluster[1-3] -b
```

Hostfile `chessbase` for `mpirun -host` command

``` console
mycluster0
mycluster1
mycluster2
mycluster3
```

bash script to execute mpirun command

``` s
#!/bin/bash
# mpirun /usr/games/stockfish15
mpirun --hostfile /home/user/chessbase /usr/games/stockfish15
# mpirun --display-allocation --hostfile chessbase /usr/games/stockfish15
```
