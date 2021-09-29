#!/bin/bash 
sudo apt-get install openssh-server openssh-client
ssh-keygen -t rsa -P ""
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
ssh localhost
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
tar -xzvf hadoop-3.3.0.tar.gz
sudo mv hadoop-3.3.0 /usr/local/hadoop/
sudo gedit ~/.bashrc
sudo gedit /usr/local/hadoop/etc/hadoop/hadoop-env.sh
sudo gedit /usr/local/hadoop/etc/hadoop/core-site.xml
sudo gedit /usr/local/hadoop/etc/hadoop/hdfs-site.xml
sudo gedit /usr/local/hadoop/etc/hadoop/mapred-site.xml
sudo gedit /usr/local/hadoop/etc/hadoop/yarn-site.xml
hadoop

