#!/bin/bash
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --db="/mnt/c/temp/rocksdbtest-1000/dbbench" --mmap_read=0 --statistics=1 --histogram=1 --threads=6 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=3600 --num=100000 --write_buffer_size=134217000 --level0_file_num_compaction_trigger=8 --level0_slowdown_writes_trigger=18 --level0_stop_writes_trigger=20 --compaction_style=0 --readwritepercent=50 --report_interval_seconds=1 --stats_interval_seconds=1 --stats_per_interval=1 --report_file="analysis/dbbenchResults/special/WriteHeavyLeveledReport.csv" 1> analysis/dbbenchResults/special/WriteHeavyLeveled.txt 2> analysis/dbbenchResults/special/IntervalWriteHeavyLeveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --db="/mnt/c/temp/rocksdbtest-1000/dbbench" --mmap_read=0 --statistics=1 --histogram=1 --threads=6 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=3600 --num=100000 --write_buffer_size=134217000 --level0_file_num_compaction_trigger=8 --level0_slowdown_writes_trigger=18 --level0_stop_writes_trigger=20 --compaction_style=1 --readwritepercent=50 --report_interval_seconds=1 --stats_interval_seconds=1 --stats_per_interval=1 --report_file="analysis/dbbenchResults/special/WriteHeavyTieredReport.csv" 1> analysis/dbbenchResults/special/WriteHeavyTiered.txt 2> analysis/dbbenchResults/special/IntervalWriteHeavyTiered.txt