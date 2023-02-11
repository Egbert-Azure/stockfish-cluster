# Stockfish Cluster Performance Test

> Note: needs to be tested in all setups (Azure cluster, SBC cluster)
> 
> Dependencies: needs Stockfish cluster version compiled with OpenMPI

This python script allows you to specify the hash size and number of threads by adding two new lists: hash_sizes and threads. The script then loops over each combination of values of -np, -map-by, hash size, and number of threads, and runs the benchmark with each combination. The results of each run of the benchmark are written to the file `results.txt`, and displayed on the screen using the print function.

``` py
import subprocess
import csv

# Constants for the benchmark
NODES = ['mycluster1', 'mycluster2', 'mycluster3']  # List of nodes to use for the benchmark
REPEAT = 3                                           # Number of times to repeat the benchmark for each setting
DEPTH = 13                                           # Depth for the Stockfish engine to search
HASH = [16, 32, 64, 128, 256, 512]                  # Hash sizes to test
THREADS = range(3, 13)                              # Number of threads to use for the benchmark

# File to save the results
filename = "results.csv"                             # File to store the results of the benchmark
header = ["Hash", "Threads", "Score"]                # Header for the csv file

# Write header to the csv file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Loop over the hash and threads values
for hash_size in HASH:
    for threads in THREADS:
        for repeat in range(REPEAT):
            # Generate the command to run the Stockfish benchmark
            command = f"mpirun -np 4 --host mycluster0,{','.join(NODES)} /usr/games/stockfish15 bench -hash {hash_size} -threads {threads} -depth {DEPTH}"

            # Run the command and get the output
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Extract the score from the output
            score = result.stdout.decode().split("\n")[-2].split()[-1]
            print(f"Hash: {hash_size} Threads: {threads} Score: {score}")

            # Write the results to the csv file
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([hash_size, threads, score])

```

With `nohup python3 scriptname.py &` you run the script in the background, even if the connection is lost, and the output of the script will be written to the file `nohup.out`.
> Note: I added a terminal output to get an idea how long it still takes. Can be removed for the final test
