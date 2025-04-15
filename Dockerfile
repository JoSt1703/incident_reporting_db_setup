FROM jupyter/pyspark-notebook:latest

# Switch to root for installing packages and writing to protected folders
USER root

# Install pymongo
RUN pip install pymongo

# Download Mongo Spark Connector JAR (compatible with Spark 3.x)
RUN wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar \
    -P /usr/local/spark/jars/

# Return to default user
USER $NB_UID
