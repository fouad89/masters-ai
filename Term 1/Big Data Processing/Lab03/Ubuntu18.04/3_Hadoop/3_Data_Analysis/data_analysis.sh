#!/bin/bash 
ssh localhost
hdfs dfs -put ./my_dataset/ /user/my_HDFS/my_dataset
# MapReduce or Spark Job Command
hdfs dfs -get /user/my_HDFS/my_result ./
hdfs dfs -rm -r /user/my_HDFS/my_dataset/
hdfs dfs -rm -r /user/my_HDFS/my_result/
