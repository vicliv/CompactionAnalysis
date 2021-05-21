#!/bin/bash

./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --db="/mnt/c/temp/rocksdbtest-1000/dbbench" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170000 --level0_file_num_compaction_trigger=5 --level0_slowdown_writes_trigger=8 --level0_stop_writes_trigger=10 --compaction_style=0 --readwritepercent=50 --report_interval_seconds=1 --report_file="analysis/dbbenchResults/long/WriteHeavyLeveledReport13.csv" > analysis/dbbenchResults/long/WriteHeavyLeveled13.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --db="/mnt/c/temp/rocksdbtest-1000/dbbench" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170000 --level0_file_num_compaction_trigger=5 --level0_slowdown_writes_trigger=8 --level0_stop_writes_trigger=10 --compaction_style=1 --readwritepercent=50 --report_interval_seconds=1 --report_file="analysis/dbbenchResults/long/WriteHeavyTieredReport13.csv" > analysis/dbbenchResults/long/WriteHeavyTiered13.txt