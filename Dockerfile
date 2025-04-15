FROM jupyter/pyspark-notebook:latest

# Install pymongo for inserting test data
RUN pip install pymongo

# Add MongoDB Spark connector JAR (compatible with Spark 3.x and Scala 2.12)
RUN wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.12/3.0.1/mongo-spark-connector_2.12-3.0.1.jar \
    -P /usr/local/spark/jars/
