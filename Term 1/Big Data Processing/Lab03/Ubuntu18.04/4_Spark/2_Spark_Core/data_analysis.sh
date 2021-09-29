#!/bin/bash 
ssh localhost
hdfs dfs -put ./my_dataset/ /user/my_HDFS/my_dataset
#
spark-submit --master yarn --deploy-mode cluster ./my_Spark_Core_example.py /user/my_HDFS/my_dataset /user/my_HDFS/my_result
#
hdfs dfs -get /user/my_HDFS/my_result ./
hdfs dfs -rm -r /user/my_HDFS/my_dataset/
hdfs dfs -rm -r /user/my_HDFS/my_result/
