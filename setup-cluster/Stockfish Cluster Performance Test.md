# Stockfish Cluster Performance Test

> Note: needs to be tested in all setups (Azure cluster, SBC cluster)
> 
> Dependencies: needs Stockfish cluster version compiled with OpenMPI

This python script allows you to specify the hash size and number of threads by adding two new lists: hash_sizes and threads. The script then loops over each combination of values of -np, -map-by, hash size, and number of threads, and runs the benchmark with each combination. The results of each run of the benchmark are written to the file `results.txt`, and displayed on the screen using the print function.

``` py
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
```

With `nohup python3 scriptname.py &` you run the script in the background, even if the connection is lost, and the output of the script will be written to the file `nohup.out`.
> Note: I added a terminal output to get an idea how long it still takes. Can be removed for the final test
