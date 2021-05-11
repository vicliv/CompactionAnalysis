#!/bin/bash

./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=0 --num_column_families=100 --num_hot_column_families=1> analysis/dbbenchResults/1%Leveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 --num_column_families=100 --num_hot_column_families=1 > analysis/dbbenchResults/1%Tiered.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=0 --readwritepercent=50 > analysis/dbbenchResults/WriteHeavyLeveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 --readwritepercent=50 > analysis/dbbenchResults/WriteHeavyTiered.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=0 --readwritepercent=95 > analysis/dbbenchResults/ReadHeavyLeveled.txt
./rocksdb/db_bench --benchmarks="readrandomwriterandom,stats" --mmap_read=0 --statistics=1 --histogram=1 --threads=2 --key_size=8 --value_size=1024 --compression_type=none --stats_interval=1000 --use_existing_db=0 --duration=10 --num=1000000000 --write_buffer_size=1342170 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=2 --compaction_style=1 --readwritepercent=95 > analysis/dbbenchResults/ReadHeavyTiered.txt

python3 analysis/src/histogram.py