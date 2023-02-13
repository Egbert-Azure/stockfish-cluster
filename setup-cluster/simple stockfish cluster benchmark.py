# simple stockfish cluster benchmark
# ver 2020-10-20
# python script to run benchmark with Stockfish on a 4 node cluster where clustermaster is the master, clusternode1 to 3 are the workers
# each node has 4 cores
# the stockfish binary is in /home/usr/stockfish15
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

# Constants for the benchmark
NODES = ['mycluster1', 'mycluster2', 'mycluster3']  # List of nodes to use for the benchmark
REPEAT = 3                                           # Number of times to repeat the benchmark for each setting
DEPTH = 13                                           # Depth for the Stockfish engine to search
HASH = [16, 32, 64, 128, 256, 512]                  # Hash sizes to test

# Function to run the benchmark with a specified hash size and number of threads
def run_benchmark(hash_size, threads):
    # Record the start time
    start = time.time()

    # Construct the command to run the benchmark using mpirun
    cmd = f"mpirun -np 4 --host mycluster0,{','.join(NODES)} /usr/games/stockfish15 bench -hash {hash_size} -threads {threads} -depth {DEPTH}"
    
    # Run the command and capture its output
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # Calculate the elapsed time
    elapsed = time.time() - start

    return elapsed

def main():
    # List of values for the hash size to test
    hash_sizes = [16, 32, 64, 128, 256, 512]

    # List of values for the number of threads to test
    threads = range(3, 13)

    # Open a file to write the results to
    with open('/home/usr/results.csv', 'w') as f:
        writer = csv.writer(f)

        # Write the header row for the file
        writer.writerow(['Hash size', 'Threads', 'Time'])

        # Loop over the values of hash size and number of threads
        for hash_size in hash_sizes:
            for t in threads:
                # Run the benchmark
                result = run_benchmark(hash_size, t)

                # Write the results to the file
                writer.writerow([hash_size, t, result])

# Call the main function if the script is run as the main program
if __name__ == '__main__':
    main()
