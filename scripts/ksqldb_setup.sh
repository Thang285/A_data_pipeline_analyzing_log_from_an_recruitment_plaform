#!/bin/bash
/etc/confluent/docker/run &
sleep 30
ksql http://ksqldb-server:8088 <<EOF
CREATE STREAM source (job_id FLOAT, date DATE, hour FLOAT, publisher_id FLOAT, campaign_id FLOAT, group_id FLOAT, ts TIMESTAMP, bid_set FLOAT, clicks FLOAT, spend_hour FLOAT, conversions FLOAT, qualified FLOAT, unqualified FLOAT, company_id FLOAT) WITH ( KAFKA_TOPIC = 'json_data', VALUE_FORMAT = 'JSON');
SET 'auto.offset.reset' = 'earliest';
CREATE STREAM target_avro WITH (VALUE_FORMAT='AVRO', KAFKA_TOPIC='avro_data') AS SELECT * FROM source;
exit
EOF
sleep infinity
