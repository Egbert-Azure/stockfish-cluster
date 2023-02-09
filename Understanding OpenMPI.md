# Understanding OpenMPI
OpenMPI is an implementation of the Message Passing Interface (MPI) standard for parallel programming. MPI is a standard for parallel programming that allows programs to run on multiple processors or computers.

This example demonstrates how to use OpenMPI to create a team of threads that execute code concurrently.

``` c
#include <stdio.h>
#include <sched.h>

int main( int argc, char**argv )
{
#pragma omp parallel
    {
        printf( "Hello world from thread %d of %d running on cpu %2d!\n", 
            omp_get_thread_num()+1, 
            omp_get_num_threads(),
            sched_getcpu());
    }
    return 0;
}
```
The code includes the header files stdio.h and sched.h, which are standard C library header files. The `main()` function takes two arguments: `argc`, which is the number of arguments passed to the program, and `argv`, which is an array of strings representing the arguments passed to the program.

The `#pragma omp` parallel directive is part of OpenMP, which is a set of directives and libraries for parallel programming in C, C++, and Fortran. The directive tells the compiler to generate code to create a team of threads to execute the code in the block concurrently.

The `omp_get_thread_num()` function returns the thread number of the current thread, where the first thread has a thread number of 0. The `omp_get_num_threads()` function returns the total number of threads in the team.

The `sched_getcpu()` function from sched.h returns the CPU number that the current thread is running on.

The code prints out a message for each thread, indicating the thread number, the total number of threads, and the CPU number that the thread is running on. The message is printed using the `printf()` function from `stdio.h`.

The return 0 statement at the end of the `main()` function returns the status code of 0, indicating that the program ran successfully.



