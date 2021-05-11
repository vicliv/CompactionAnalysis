#!/bin/bash

chmod -R +xwr rocksdb
cd rocksdb
make clean
make DEBUG_LEVEL=0 -j4 db_bench

./db_bench --benchmarks=readrandomwriterandom --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 > ../analysis/dbbenchResults/result2.txt