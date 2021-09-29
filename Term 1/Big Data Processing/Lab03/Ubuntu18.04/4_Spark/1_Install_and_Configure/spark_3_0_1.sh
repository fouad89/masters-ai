#!/bin/bash 
wget https://downloads.apache.org/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
tar -xzvf spark-3.0.1-bin-hadoop3.2.tgz
sudo mv spark-3.0.1-bin-hadoop3.2 /usr/local/spark
python3.9 -m pip install pyspark
sudo gedit ~/.bashrc
spark-submit --version
