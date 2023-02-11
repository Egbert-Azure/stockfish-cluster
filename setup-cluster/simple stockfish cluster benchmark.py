#simple stockfish cluster benchmark

import subprocess
import time

import subprocess
import time

# Function to run the benchmark with a specified number of processes and mapping
def run_benchmark(np, map_by):
    # Record the start time
    start = time.time()

    # Construct the command to run the benchmark using mpirun
    cmd = f'mpirun -hosts mycluster0,mycluster1,mycluster2,mycluster3 -map-by {map_by} /usr/games/stockfish15 bench -np {np}'

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

    # Open a file to write the results to
    with open('results.txt', 'w') as f:
        # Loop over the values of -np and -map-by
        for np in nps:
            for map_by in map_bys:
                # Write the header for this run of the benchmark
                f.write(f'Running benchmark with -np {np} -map-by {map_by}\n')
                print(f'Running benchmark with -np {np} -map-by {map_by}')

                # Run the benchmark and write the result
                result = run_benchmark(np, map_by)
                f.write(f'Elapsed time: {result} seconds\n')
                print(f'Elapsed time: {result} seconds')

# Call the main function if the script is run as the main program
if __name__ == '__main__':
    main()
