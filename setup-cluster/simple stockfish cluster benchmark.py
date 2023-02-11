#simple stockfish cluster benchmark
# ver 2

import subprocess
import csv

# Constants for the benchmark
NODES = ['mycluster1', 'mycluster2', 'mycluster3']
REPEAT = 3
DEPTH = 13
HASH = [16, 32, 64, 128, 256, 512]
THREADS = range(3, 13)

# File to save the results
filename = "results.csv"
header = ["Hash", "Threads", "Score"]

# Write header to the csv file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)

# Loop over the hash and threads values
for hash_size in HASH:
    for threads in THREADS:
        for repeat in range(REPEAT):
            command = f"mpirun -np 4 --host mycluster0,{','.join(NODES)} /usr/games/stockfish15 bench -hash {hash_size} -threads {threads} -depth {DEPTH}"
            result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            score = result.stdout.decode().split("\n")[-2].split()[-1]
            print(f"Hash: {hash_size} Threads: {threads} Score: {score}")

            # Write the results to the csv file
            with open(filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([hash_size, threads, score])
