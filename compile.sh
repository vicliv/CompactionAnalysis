#!/bin/bash

chmod -R +xwr rocksdb
cd rocksdb
make clean
make DEBUG_LEVEL=0 -j4 db_bench