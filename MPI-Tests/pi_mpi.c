/*
  pi_mpi.c
  Author: Egbert Schroeer
  Goal: To demonstrate how to use MPI to calculate the value of pi in parallel on multiple nodes.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

#define MAX_ITER 100000000

int main(int argc, char *argv[]) {
    int node_num_iter, in_circle_count = 0, total_in_circle_count = 0;
    int rank, size;
    double x, y, pi, start_time, end_time;
    char node_name[MPI_MAX_PROCESSOR_NAME];
    int node_name_len;

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Get_processor_name(node_name, &node_name_len);

    if (size != 4) {
        if (rank == 0) {
            printf("This program must be run with 4 nodes.\n");
        }
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    node_num_iter = MAX_ITER / size;
    srand(time(NULL) + rank);

    start_time = MPI_Wtime();
    for (int i = 0; i < node_num_iter; i++) {
        x = (double) rand() / RAND_MAX;
        y = (double) rand() / RAND_MAX;

        if (x * x + y * y <= 1.0) {
            in_circle_count++;
        }
    }
    MPI_Reduce(&in_circle_count, &total_in_circle_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        pi = 4.0 * total_in_circle_count / MAX_ITER;
        end_time = MPI_Wtime();
        printf("Value of pi: %.10f\n", pi);
        printf("Number of nodes: %d\n", size);
        for (int i = 0; i < size; i++) {
            MPI_Get_processor_name(node_name, &node_name_len);
            printf("Node name %d: %s\n", i, node_name);
        }
        printf("Time used: %f seconds\n", end_time - start_time);
    }

    MPI_Finalize();
    return 0;
}
