#!/bin/bash 
ssh localhost
hdfs namenode -format
start-dfs.sh
start-yarn.sh
hdfs dfs -mkdir /user/
hdfs dfs -mkdir /user/my_HDFS/


