# Install the Stockfish Cluster Engine
Now that you have your cluster up and running on either a single board computer or on Azure, it's time to move onto the installation of the cluster version of the Stockfish chess engine. This version uses parallel computing with OpenMPI to connect processes running on multiple computers and allow them to communicate with each other as they run. This allows you to run a single script across multiple cluster nodes.

## Dependencies:
- openmpi-bin
- openmpi-common
- libopenmpi3
- libopenmpi-dev

First, you'll need to clone the Stockfish Cluster branch:

We only need to clone the Stockfish Cluster branch:
``` clone
$ git clone --branch cluster --single-branch https://github.com/official-stockfish/Stockfish.git cluster
```
Next step is to compile the cluster version with the make file.
``` consol
$ cd cluster
$ make build ARCH=x86-64-modern-Haswell COMPILER=mpicxx
```
Note: The ARCH flag can be set to a variety of different architectures, depending on your setup. The x86-64-modern-Haswell architecture is just an example and may not be appropriate for your particular setup. The COMPILER=mpicxx syntax specifies that you want to use the MPI compiler
