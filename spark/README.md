

<img src="https://www.databricks.com/wp-content/uploads/2019/02/largest-open-source-apache-spark.png" style="height:300px" />


# Hadoop
 Hadoop is an open source framework that helps to store, process and analyze a large volume of data.

# Apache Spark
Apache Spark is another **cluster computing framework** like Hadoop which is used to analyze a huge dataset, but it’s much faster as compared to Hadoop which makes it ideal for today’s high computing needs like processing huge amounts of data. 

# Spark vs Hadoop
Hadoop and Spark are two frameworks providing tools for carrying out big-data related tasks. While Spark is faster than Hadoop, Spark has one drawback. It lacks a distributed storage system. In other words, Spark lacks a system to organize, store and process data files.

# What is HDFS?
 HDFS  (Hadoop Distributed File System)  is the distributed file system of Hadoop that provides high throughput access to application data.

# MapReduce System
HDFS uses MapReduce system as a resource manager to allow the distribution of the files across the hard drives within the cluster. Think of it as the MapReduce System storing the data back on the hard drives after completing all the tasks.

Spark, on the other hand, runs the operations and holds the data in the RAM memory rather than the hard drives used by HDFS. Since Spark lacks a file distribution system to organize, store and process data files, Spark tools are often installed on Hadoop because Spark can then use the Hadoop Distributed File System (HDFS).


#  RDDs Resilient Distributed Data Set
RDDs are a low-level abstraction of the data. In the first version of Spark, you worked directly with RDDs. You can think of RDDs as long lists distributed across various machines. You can still use RDDs as part of your Spark code although data frames and SQL are easier


# From local mode to cluster
Spark provides 3 options for working on a cluster.

Standaline Mode
MESOS
YARN
Mesos and Yarn are for sharing a Spark cluster across an entire team of engineers and analysts.


# Resources 
*   [Free courses to learn spark](!https://medium.com/javarevisited/5-free-courses-to-learn-apache-spark-in-2020-bdff2d60c800)
* [Comparison of Hadoop, Spark and Kafka](!https://www.techtarget.com/searchdatacenter/feature/Compare-Hadoop-vs-Spark-vs-Kafka-for-your-big-data-strategy)
