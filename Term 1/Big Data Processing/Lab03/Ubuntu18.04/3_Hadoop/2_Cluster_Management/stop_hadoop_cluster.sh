#!/bin/bash 
ssh localhost
hdfs dfs -rm -r /user
stop-yarn.sh
stop-dfs.sh


