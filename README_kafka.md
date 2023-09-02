# Kafka 
### Go to the directory of kafka
### Start zoo keeper
```.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties```
### Start kafka server
```.\bin\windows\kafka-server-start.bat .\config\server.properties```
### Create kafka topic - kafka topic name: "hrproject"
```.\bin\windows\kafka-topics.bat --create --bootstrap-server 192.168.56.1:9092 --replication-factor 1 --partitions 1 --topic hrproject```
### Send log data to kafka topic
``` Run script "kafka/fake_data_to_kafka_producer.py"```
### Read data from kafka topic and storage in  Cassandra
``` Run script "kafka/Write_data_from_kafka_topic_to_cassandra.py"```
