#!/bin/bash
/etc/confluent/docker/run & 
confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.4
sleep 10
cd /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc
mkdir jar_file
cd jar_file
wget -nc https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar
sleep 60
/usr/bin/connect-standalone /etc/schema-registry/connect-avro-standalone.properties /etc/kafka/jdbc_sink_config.properties
sleep infinity
