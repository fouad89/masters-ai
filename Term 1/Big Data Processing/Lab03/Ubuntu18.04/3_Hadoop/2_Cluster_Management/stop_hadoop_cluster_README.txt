----------------------------------------------------------------------------

 HADOOP 3.2.1. CLOSE CLUSTER

----------------------------------------------------------------------------

In this section we discuss how to close a cluster in Hadoop 2.7.1.

---------------------------------------------------------
(1) $ ssh localhost
---------------------------------------------------------

We connect by ssh without a passphrase.

---------------------------------------------------------
(2) $ hdfs dfs -rm -r /user
---------------------------------------------------------

We delete our HDFS folder

Deleted /user

---------------------------------------------------------
(3) $ stop-yarn.sh
---------------------------------------------------------

We stop the job scheduler Yarn, specifically its ResourceManager and NodeManager daemons.

stopping yarn daemons
stopping resourcemanager
localhost: stopping nodemanager
localhost: nodemanager did not stop gracefully after 5 seconds: killing with kill -9
no proxyserver to stop

---------------------------------------------------------
(4) $ stop-dfs.sh
---------------------------------------------------------

We stop the NameNode and DataNode daemons.

Stopping namenodes on [localhost]
localhost: stopping namenode
localhost: stopping datanode
Stopping secondary namenodes [0.0.0.0]
0.0.0.0: stopping secondarynamenode





