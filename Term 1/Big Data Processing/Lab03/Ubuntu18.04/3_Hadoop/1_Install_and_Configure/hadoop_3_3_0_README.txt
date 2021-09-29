----------------------------------------------------------------------------

 HADOOP 3.3.0. INSTALLATION

----------------------------------------------------------------------------

In this section we discuss how to install Hadoop 3.3.0.

---------------------------------------------------------
(1) $ sudo apt-get install openssh-server openssh-client
---------------------------------------------------------
(2) $ ssh-keygen -t rsa -P ""
---------------------------------------------------------

It outputs the following content:

Generating public/private rsa key pair.
Enter file in which to save the key (/home/nacho/.ssh/id_rsa): 
Your identification has been saved in /home/nacho/.ssh/id_rsa.
Your public key has been saved in /home/nacho/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:iG3re7Qjwi4I8Dq+oDlOISUv44LfdEdhVCbJUHHFKTE nacho@com-a284-x51877
The key's randomart image is:
+---[RSA 2048]----+
|      .+=+E+..   |
|       .o+..o    |
|. .     o  .     |
|.+   o o .       |
|=o. . + S        |
|=oo  . o.        |
|== .. o...       |
|Xo.ooo..+        |
|=*ooo.o+ .       |
+----[SHA256]-----+

---------------------------------------------------------
(3) $ cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
---------------------------------------------------------
(4) ssh localhost
---------------------------------------------------------

Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-99-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Ubuntu 20.04 LTS is out, raising the bar on performance, security,
   and optimisation for Intel, AMD, Nvidia, ARM64 and Z15 as well as
   AWS, Azure and Google Cloud.

     https://ubuntu.com/blog/ubuntu-20-04-lts-arrives


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.

Last login: Sat May  9 12:02:01 2020 from 127.0.0.1

---------------------------------------------------------
(5) $ wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
---------------------------------------------------------
(6) $ tar -xzvf hadoop-3.3.0.tar.gz
---------------------------------------------------------
(7) $ sudo mv hadoop-3.3.0 /usr/local/hadoop/
---------------------------------------------------------
(8) $ sudo gedit ~/.bashrc
---------------------------------------------------------
Add the following lines

export PATH=$PATH:/usr/local/hadoop/bin/:/usr/local/hadoop/sbin/
#
export HADOOP_HOME=/usr/local/hadoop/
export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
export HADOOP_MAPRED_HOME=/usr/local/hadoop/
export HADOOP_COMMON_HOME=/usr/local/hadoop/
export HADOOP_HDFS_HOME=/usr/local/hadoop/
export YARN_HOME=/usr/local/hadoop/
export HADOOP_COMMON_LIB_NATIVE_DIR=/usr/local/hadoop/lib/native
export HADOOP_OPTS="-Djava.library.path=/usr/local/hadoop/lib"

---------------------------------------------------------
(9) $ sudo gedit /usr/local/hadoop/etc/hadoop/hadoop-env.sh
---------------------------------------------------------

We add the line: 
export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64

---------------------------------------------------------
(10) $ sudo gedit /usr/local/hadoop/etc/hadoop/core-site.xml
---------------------------------------------------------

Replace the last two lines: 
<configuration>
</configuration>

With the following content:
<configuration>
	<property>
		<name>fs.defaultFS</name>
		<value>hdfs://localhost:9000</value>
	</property>
</configuration>

---------------------------------------------------------
(11) $ sudo gedit /usr/local/hadoop/etc/hadoop/hdfs-site.xml
---------------------------------------------------------

Replace the last two lines: 
<configuration>
</configuration>

With the following content:
<configuration>
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
</configuration>

---------------------------------------------------------
(12) $ sudo gedit /usr/local/hadoop/etc/hadoop/mapred-site.xml
---------------------------------------------------------

Replace the last two lines: 
<configuration>
</configuration>

With the following content:
<configuration>
	<property>
		<name>mapreduce.framework.name</name>
		<value>yarn</value>
	</property>
    	<property>
        	<name>mapreduce.application.classpath</name>
        	<value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    	</property>
</configuration>

---------------------------------------------------------
(13) $ sudo gedit /usr/local/hadoop/etc/hadoop/yarn-site.xml
---------------------------------------------------------

Replace the last two lines: 
<configuration>
</configuration>

With the following content:
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>

---------------------------------------------------------
(14) $ hadoop
---------------------------------------------------------

We trigger Hadoop 3.3.0
