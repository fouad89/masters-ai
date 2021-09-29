#!/bin/bash 
ssh localhost
hdfs dfs -put ./my_dataset/ /user/my_HDFS/my_dataset
#
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
-input /user/my_HDFS/my_dataset \
-output /user/my_HDFS/my_result \
-mapper ./my_mapper.py \
-reducer ./my_reducer.py \
-file ./my_mapper.py \
-file ./my_reducer.py
#
hdfs dfs -get /user/my_HDFS/my_result ./
hdfs dfs -rm -r /user/my_HDFS/my_dataset/
hdfs dfs -rm -r /user/my_HDFS/my_result/
