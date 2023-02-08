# MPI Parallel Pi Calculation
<h2>Introduction</h2>
This program uses MPI (Message Passing Interface) to calculate the value of pi in parallel on multiple nodes. It performs a Monte Carlo simulation to estimate the value of pi and reduces the results from all nodes to calculate the final value.

<h2>Code Explanation</h2>
The code starts by initializing MPI and obtaining the rank and size of the nodes. If the program is not being run with 4 nodes, it aborts with an error message.

Each node then performs `node_num_iter` iterations of the Monte Carlo simulation, where node_num_iter is equal to `MAX_ITER / size`, and `MAX_ITER` is a constant defined as 100,000,000. For each iteration, a random x and y value are generated and checked if they lie within the unit circle. If they do, the count of points inside the unit circle is incremented.

After all nodes have completed their simulations, the `in_circle_count` from each node is reduced to a single `value total_in_circle_count` on `node 0` using the `MPI_Reduce` function. `Node 0` then calculates the final value of pi as `4.0 * total_in_circle_count / MAX_ITER`.

Finally, node 0 outputs the value of pi, the time used, the number of nodes, and the node names.

<b>Usage</b>

To run the program, compile it using an MPI compiler, such as mpicc, and run it using an MPI runner, such as mpirun, with 4 nodes:

```console
mpicc pi_mpi.c -o pi_mpi
mpirun -np 4 pi_mpi
```
<b>Output</b>

The program outputs the following information:

``` yaml
Value of pi: 3.1415926536
Number of nodes: 4
Node names: node1 node2 node3 node4
Time used: 0.234567 seconds
```
<b>Goal</b>

To demonstrate how to use MPI to calculate the value of pi in parallel on multiple nodes.