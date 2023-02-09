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