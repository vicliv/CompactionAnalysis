# Compaction Analysis
Research project to find efficient compaction policies on a RocksDB database on different workload profiles.

Leveled and Tiered compaction policies were both tested on a:
- Write heavy workload with 50% reads and 50% writes uniformaly distributed
- Read heavy workload with 95% reads and 5% writes uniformaly distributed
- A Zipfian (1%, alpha = 0.99) distribution with a write heavy workload
- A Zipfian (1%, alpha = 0.99) distribution with a write read workload


## Installation

You will need to install the following ressources to be able to run replicate the results.
First make sure python with matplotlib and C++ are installed. Check documentation if needed.

#### RocksDB:
RocksDB v6.20.3 https://github.com/facebook/rocksdb/releases/tag/v6.20.3 was used and modified for this project.
dbbench was modified to have an optional Zipfian distribution (boolean parameter `zipfian` for readrandomwriterandom only) and more statistics as ouput.
Make sure you have everything installed to run dbbench properly (GFLAGS, gcc make, C++)
The added statistics are for each interval:
- Read histogram by interval
- Write histohram by interval
- Number of written bytes during compaction per intervals
These statistics are activated when the parameter stats_interval_seconds is used
Each picked keys are also now printed to the file analysis/keys.txt to check the distribution. This would be useful for future work.

#### Python:
Python 3.6+ with matplotlib needs to be installed

## Compiles
`compile.sh` compiles RocksDB in case some things were changed in its code.

## Running
Run `run.sh` with the command ./run.sh from the terminal within the CompactionAnalysis directory. It will run the command used the get the results in this experiment. Note that the tests were made on a 3.2 Ghz 6 cores CPU and can be very different on other computer. The main point the retain is the difference between Leveled and Tiered compaction policies on the 4 different workloads tested. The advantage and inconvenience of both policies should remain the same on different computers that as a decent amount of ram.

The run.sh file might not work on a Windows OS, I recommand getting a Unix virtual machine to run it as Ubuntu.

Other test runs are in the directory `/runs` that were not used directly in the final report but were used to find the best parameters.

## Plotting
You can plot some results from the tests with the python files in `/analysis/src`, I recommend reading the comments in them to figure out what they do.
Note that some of the functions might not work as some directory were changed and these functions were not used in the final report.
The plots are using the results in `/analysis/src/dbbenchResults` and are outputed in `/analysis/src/plots`
