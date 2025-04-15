FROM jupyter/pyspark-notebook:latest

USER root

# Install pymongo for inserting data in Python
RUN pip install pymongo

# Add MongoDB Spark Connector and its Java driver dependency
RUN wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar \
    -P /usr/local/spark/jars/ && \
    wget https://repo1.maven.org/maven2/org/mongodb/mongo-java-driver/3.12.10/mongo-java-driver-3.12.10.jar \
    -P /usr/local/spark/jars/

USER $NB_UID
