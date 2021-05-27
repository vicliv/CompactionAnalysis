# Compaction Analysis
Research project to find efficient compaction policies on a RocksDB database on different workload profiles


## Installation

You will need to install the following ressources to be able to run replicate the results.
First make sure python with matplotlib and C++ are installed. Check documentation if needed

#### RocksDB:
RocksDB v6.20.3 https://github.com/facebook/rocksdb/releases/tag/v6.20.3 was used and modified for this project.
dbbench wad modified to have an optional zipfian distribution and more statistics as ouput.
Make sure you have everything installed to run dbbench properly (GFLAGS, gcc make, C++)

#### Python:
Python 3.6+ with matplotlib needs to be installed

## Running
Run run.sh with the command ./run.sh from the terminal within the CompactionAnalysis directory. It will run the command used the get the results in this experiment. Note that the tests were made on a 3.4 Ghz 6 cores CPU and can be very different on other computer. The main point the retain is the difference between leveled and tiered compaction policies on the 4 different workloads tested. The advantage and inconvenience of both policies should remain the same on different computers that as a decent amount of ram.

The run.sh file might not work on a Windows OS, I recommand getting a Unix emulator to run it.
