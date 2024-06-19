#!/bin/bash
/etc/confluent/docker/run &
sleep 10
/usr/bin/kafka-topics --create --bootstrap-server broker:29092 --replication-factor 1 --partitions 1 --topic json_data --if-not-exists
/usr/bin/kafka-topics --create --bootstrap-server broker:29092 --replication-factor 1 --partitions 1 --topic avro_data --if-not-exists
sleep infinity
