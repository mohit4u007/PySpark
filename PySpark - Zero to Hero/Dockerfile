FROM python:3.12
# Copy the requirements.txt file into the container
COPY requirements.txt .
# Upgrade pip
RUN pip install --upgrade pip
# Install additional packages
RUN pip install -r requirements.txt

# Install OpenJDK default
RUN apt-get update && apt-get -y install openjdk-21-jdk && apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin

# Lines below will be uncommented when you want to practice cluster mode
# Download and Setup Spark binaries
WORKDIR /tmp
RUN apt-get update && apt-get install -y wget && apt-get clean
RUN wget https://archive.apache.org/dist/spark/spark-3.5.7/spark-3.5.7-bin-hadoop3.tgz
RUN tar -xvf spark-3.5.7-bin-hadoop3.tgz
RUN mv spark-3.5.7-bin-hadoop3 spark
RUN mv spark /
RUN rm spark-3.5.7-bin-hadoop3.tgz

# Set up environment variables
ENV SPARK_HOME=/spark
RUN export SPARK_HOME
ENV PYSPARK_PYTHON=/usr/local/bin/python
RUN export PYSPARK_PYTHON
ENV PYTHONPATH=$SPARK_HOME/python
RUN export PYTHONPATH
ENV PATH=$PATH:$SPARK_HOME/bin
RUN export PATH

# Fix configuration files
RUN mv $SPARK_HOME/conf/log4j2.properties.template $SPARK_HOME/conf/log4j2.properties
RUN mv $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf
RUN mv $SPARK_HOME/conf/spark-env.sh.template $SPARK_HOME/conf/spark-env.sh

WORKDIR /data

# Add a log running command to sustain the container
CMD ["tail", "-f", "/dev/null"]