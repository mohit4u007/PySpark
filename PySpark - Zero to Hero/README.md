Basics of pyspark library is discussed and practiced in this repo.
Spark is for big data and all data activities can be done on a distributed environment or on cluster of systems may be on cloud.
pyspark - spark api with python
Spark can run on Hadoop, Apache Mesos, Kubernetes, standalone or in the cloud. It can access diverse data sources.
Databricks is the platform to run pyspark programs in a distributed env using the community login.
Its an open and unified data analytics platofrm for data engineering, data science, machine learning and analytics.
Spark is open source unified computing engine with set of libraries for parallel data processing on computer cluster.
spark uses RAM for data processing whereas traditional hadoop map redue uses disk to write data during processing
low level api -> structured api -> libraries and ecosystem
rdd (resiliant distributed data) and distributed variables -> dataframes datasets and sql -> structured streaming and advanced analytics
Driver, Executor, Shuffle, Local and Global stage
Driver - Manages the information and state of executors. Analyses distrubites and schedules the work for executors
Executors are JVM processes. Cores of executors
To allow every executors to work in parallel, Spark breaks down the data into chunks called partisians.
Transformation: The instruction or code to modify and transform data is known as transformation. 1. Narrow and 2. Wide transformation
To trigger the execution we need to call an action. This executes the plan created by Transformation.
3 types of actions:
1. View data in console
2. Collect data to native language
3. Write data to output data sources
Spark session: The driver process is known as Spark Session, it is the entry point for a spark execution. The spark session instance executes the code in the cluster. For one spark application there can be only one spark session.
Datafame is the most common structured API represented like a table. DF has a schema which is the metadata for the columns. Data in DFs are in partitions and DFs are immutable.
DF in 4 data partitions -> transformation -> action is applied
How spark work on planning for the structured APIs - Execution Plan Phases 1. Logical Plan 2. Physical Plan
Code by user -> Unresolved logical plan -> Validated against a catalogue, col and table names are validated -> Resolved logical plan -> Taken into the catalyst optimizer -> generates a optimized logical plan
mutiple physical plan based on cluster and physical configuration -> runs against a cost model -> Best Physical plan is selected and sent to cluster for execution
Directed Acyclic Graph
RDD: Resiliant distributed data