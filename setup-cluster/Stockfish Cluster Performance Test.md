# Stockfish Cluster Performance Test

> Note: needs to be tested in all setups (Azure cluster, SBC cluster)
> Dependencies: needs Stockfish cluster version compiled with OpenMPI

This python script allows you to specify the hash size and number of threads by adding two new lists: hash_sizes and threads. The script then loops over each combination of values of -np, -map-by, hash size, and number of threads, and runs the benchmark with each combination. The results of each run of the benchmark are written to the file `results.txt`, and displayed on the screen using the print function.

``` py
import subprocess
import time

# Function to run the benchmark with a specified number of processes, mapping, hash size, and number of threads

def run_benchmark(np, map_by, hash_size, threads):
    # Record the start time
    start = time.time()

    # Construct the command to run the benchmark using mpirun
    cmd = f'mpirun -hosts mycluster0,mycluster1,mycluster2,mycluster3 -map-by {map_by} /usr/games/stockfish15 bench hash={hash_size} threads={threads} -np {np}'

    # Run the command and capture its output
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Record the end time
    end = time.time()

    # Return the elapsed time
    return end - start

# Main function to run the benchmarks and display the results
def main():
    # List of values of -np to test
    nps = [1, 2, 4, 8, 16]

    # List of values of -map-by to test
    map_bys = ['node', 'core', 'socket']

    # List of values for the hash size to test
    hash_sizes = [16, 32, 64, 128, 256]

    # List of values for the number of threads to test
    threads = [1, 2, 4, 8, 16]

    # Open a file to write the results to
    with open('results.txt', 'w') as f:
        # Loop over the values of -np, -map-by, hash size, and number of threads
        for np in nps:
            for map_by in map_bys:
                for hash_size in hash_sizes:
                    for t in threads:
                        # Write the header for this run of the benchmark
                        f.write(f'Running benchmark with -np {np} -map-by {map_by} hash={hash_size} threads={t}\n')
                        print(f'Running benchmark with -np {np} -map-by {map_by} hash={hash_size} threads={t}')

                        # Run the benchmark and write the result
                        result = run_benchmark(np, map_by, hash_size, t)
                        f.write(f'Elapsed time: {result} seconds\n')
                        print(f'Elapsed time: {result} seconds')

# Call the main function if the script is run as the main program
if __name__ == '__main__':
    main()
