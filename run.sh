#!/bin/bash

./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=0 --readwritepercent=50 --report_interval_seconds=10 --report_file="analysis/dbbenchResults/long/WriteHeavyLeveledReport.csv" > analysis/dbbenchResults/long/WriteHeavyLeveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 --readwritepercent=50 --report_interval_seconds=10 --report_file="analysis/dbbenchResults/long/WriteHeavyTieredReport.csv" > analysis/dbbenchResults/long/WriteHeavyTiered.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=0 --readwritepercent=95 --report_interval_seconds=10 --report_file="analysis/dbbenchResults/long/ReadHeavyLeveledReport.csv" > analysis/dbbenchResults/long/ReadHeavyLeveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=600 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 --readwritepercent=95 --report_interval_seconds=10 --report_file="analysis/dbbenchResults/long/ReadHeavyTieredReport.csv" > analysis/dbbenchResults/long/ReadHeavyTiered.txt