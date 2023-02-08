/*
  pi_mpi.c
  Author: Egbert Schroeer
  Goal: To demonstrate how to use MPI to calculate the value of pi in parallel on multiple nodes.
*/

#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <time.h>

#define MAX_ITER 100000000

int main(int argc, char** argv) {
  int rank, size;
  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  // Check if the program is being run with 4 nodes.
  if (size != 4) {
    printf("Error: This program must be run with 4 nodes.\n");
    MPI_Abort(MPI_COMM_WORLD, 1);
  }

  int node_num_iter = MAX_ITER / size;
  int in_circle_count = 0;
  srand(time(NULL) + rank);

  double start_time = MPI_Wtime();

  int i;
  // Monte Carlo simulation to estimate the value of pi.
  for (i = 0; i < node_num_iter; i++) {
    double x = (double) rand() / RAND_MAX;
    double y = (double) rand() / RAND_MAX;
    if (x * x + y * y <= 1) {
      in_circle_count++;
    }
  }

  int total_in_circle_count = 0;
  MPI_Reduce(&in_circle_count, &total_in_circle_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

  double pi;
  if (rank == 0) {
    // Combine the results from all nodes to calculate the final value of pi.
    pi = 4.0 * total_in_circle_count / MAX_ITER;
    printf("Value of pi: %.10f\n", pi);
    printf("Number of nodes: %d\n", size);
    printf("Node names: ");
    int i;
    for (i = 0; i < size; i++) {
      char name[MPI_MAX_PROCESSOR_NAME];
      int name_len;
      MPI_Get_processor_name(name, &name_len);
      printf("%s ", name);
    }
    printf("\n");
  }

  double end_time = MPI_Wtime();
  if (rank == 0) {
    printf("Time used: %f seconds\n", end_time - start_time);
  }

  MPI_Finalize();
  return 0;
}


