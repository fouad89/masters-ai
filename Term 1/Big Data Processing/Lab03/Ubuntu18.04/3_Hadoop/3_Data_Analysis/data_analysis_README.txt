----------------------------------------------------------------------------

 HADOOP 3.2.1. START CLUSTER

----------------------------------------------------------------------------

In this section we discuss how to start a cluster in Hadoop 2.7.1.

---------------------------------------------------------
(1) $ ssh localhost
---------------------------------------------------------

We connect by ssh without a passphrase.

---------------------------------------------------------
(2) $ hdfs namenode -format
---------------------------------------------------------

We format the filesystem. 

STARTUP_MSG: Starting NameNode
STARTUP_MSG:   host = ***MACHINE_NAME***/127.0.1.1
STARTUP_MSG:   args = [-format]
STARTUP_MSG:   version = 2.7.1
STARTUP_MSG:   classpath =
STARTUP_MSG:   java = 1.8.0_252
SHUTDOWN_MSG: Shutting down NameNode at ***MACHINE_NAME***/127.0.1.1

---------------------------------------------------------
(3) $ start-dfs.sh
---------------------------------------------------------

We start the NameNode and DataNode daemons. 

Starting namenodes on [localhost]
localhost: starting namenode, logging to /usr/local/hadoop/logs/hadoop-***USER_NAME***-namenode-***MACHINE_NAME***.out
localhost: starting datanode, logging to /usr/local/hadoop/logs/hadoop-***USER_NAME***-***MACHINE_NAME***.out
Starting secondary namenodes [0.0.0.0]
0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop/logs/hadoop-***USER_NAME***-secondarynamenode-***MACHINE_NAME***.out

---------------------------------------------------------
(4) $ start-yarn.sh
---------------------------------------------------------

We start the job scheduler Yarn, specifically its ResourceManager and NodeManager daemons.

starting yarn daemons
starting resourcemanager, logging to /usr/local/hadoop/logs/yarn-***USER_NAME***-resourcemanager-***MACHINE_NAME***.out
localhost: starting nodemanager, logging to /usr/local/hadoop/logs/yarn-***USER_NAME***-nodemanager-***MACHINE_NAME***.out

---------------------------------------------------------
(5) $ hdfs dfs -mkdir /user/
---------------------------------------------------------

We create the Hadoop Distributed File System folder /user

---------------------------------------------------------
(6) $ hdfs dfs -mkdir /user/my_HDFS/
---------------------------------------------------------

We create the Hadoop Distributed File System folder /user/my_HDFS

