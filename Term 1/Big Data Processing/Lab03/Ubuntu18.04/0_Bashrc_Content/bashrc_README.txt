#
# ---------------------------
# PATH VARIABLE
# ---------------------------
#
export PATH=$PATH:~/.local/bin:~/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
#
# ---------------------------
# JAVA
# ---------------------------
#
export PATH=$PATH:/usr/lib/jvm/java-1.11.0-openjdk-amd64/bin/
export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
export JAVA_LIBRARY_PATH=/usr/local/hadoop/lib/native:$JAVA_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
#
# ---------------------------
# PYCHARM
# ---------------------------
#
export PATH=$PATH:/usr/local/pycharm/bin/
#
# ---------------------------
# HADOOP
# ---------------------------
#
export PATH=$PATH:/usr/local/hadoop/bin/:/usr/local/hadoop/sbin/
#
# If you want to run a Spark Job with Yarn and HDFS => Next lines should be available.
# If you want to run Spark with the Standalone Scheduler and the Local File System => Next lines should be commented.
#
#export HADOOP_HOME=/usr/local/hadoop/
#export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
#export HADOOP_MAPRED_HOME=/usr/local/hadoop/
#export HADOOP_COMMON_HOME=/usr/local/hadoop/
#export HADOOP_HDFS_HOME=/usr/local/hadoop/
#export YARN_HOME=/usr/local/hadoop/
#export HADOOP_COMMON_LIB_NATIVE_DIR=/usr/local/hadoop/lib/native
#export HADOOP_OPTS="-Djava.library.path=/usr/local/hadoop/lib"
#
# ---------------------------
# SPARK
# ---------------------------
#
export PATH=$PATH:/usr/local/spark/bin/
export SPARK_HOME=/usr/local/spark
export PYSPARK_PYTHON=/usr/local/bin/python3.8
export PYSPARK_DRIVER_PYTHON=/usr/local/bin/python3.8
#
