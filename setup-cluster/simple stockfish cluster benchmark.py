#simple stockfish cluster benchmark
# ver 2020-10-20
# write python script to run benchmark with Stockfish on a 4 node cluster where clustermaster is the master, clusternode1 to 3 are the workers
# each node has 1 cpu with 4 cores
# the stockfish binary is in /home/usr/stockfish15
# it's the stockfish cluster version
# benchmark should be run 3 times with HASH in 16 32 64 128 256 512 and THREADS in {3..12}
# mpirun is -map-by node
# write the results to a file in /home/usr/results.csv on csv format
# the results should be in the form of a table with the following columns:
# HASH, THREADS, NODE, TIME
# where NODE is the name of the node the benchmark was run on
# TIME is the time in seconds it took to complete the benchmark
# the order of the results should be the same as the order of the benchmarks in the script
# the script should not use more than 1 cpu core on the master node
# the script should be run with mpirun -np 4 python3 /home/usr/benchmark.py

import subprocess
import time
import csv


# Function to run the benchmark with a specified number of processes, mapping, hash size, and number of threads
def run_benchmark(np, map_by, hash_size, threads):
    # Record the start time
    start = time.time()

    # Construct the command to run the benchmark using mpirun
    cmd = f'mpirun -hosts clustermaster,clusternode1,clusternode2,clusternode3 -map-by {map_by} /home/usr/stockfish15 bench hash={hash_size} threads={threads} -np {np}'

    # Run the command and capture its output
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Calculate the elapsed time
    elapsed = time.time() - start

    return elapsed

def main():
    # Number of processes to run the benchmark with
    nps = [1, 2, 4, 8, 16]

    # List of values for the hash size to test
    hash_sizes = [16, 32, 64, 128, 256, 512]

    # List of values for the number of threads to test
    threads = range(3, 13)

    # Open a file to write the results to
    with open('/home/usr/results.csv', 'w') as f:
        writer = csv.writer(f)

        # Write the header row for the file
        writer.writerow(['NP', 'Hash size', 'Threads', 'Time'])

        # Loop over the values of -np, hash size, and number of threads
        for np in nps:
            for hash_size in hash_sizes:
                for t in threads:
                    # Run the benchmark
                    result = run_benchmark(np, 'node', hash_size, t)

                    # Write the results to the file
                    writer.writerow([np, hash_size, t, result])

# Call the main function if the script is run as the main program
if __name__ == '__main__':
    main()
