from kafka import KafkaConsumer
from cassandra.cluster import Cluster
import json
import multiprocessing
import logging 
import sys
root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def consume_data_from_kafka(keyspace, kafka_topic, kafka_bootstrap_severs ):
    cluster = Cluster()
    session = cluster.connect(keyspace)
    consumer = KafkaConsumer(kafka_topic, bootstrap_servers= kafka_bootstrap_severs, value_deserializer=lambda v: json.loads(v.decode('utf-8')), group_id = "test-consumer-group", auto_offset_reset = "earliest", )
    consumer.poll(timeout_ms=2000)
    for message in consumer:
        data = message.value
        data = message.value
        query = """INSERT INTO tracking (create_time,bid,campaign_id,custom_track,group_id,job_id,publisher_id,ts) VALUES ('{}',{},{},'{}',{},{},{},'{}')""".format(data["create_time"], data["bid"], data["campaign_id"], data["custom_track"], data["group_id"], data["job_id"], data["publisher_id"], data["ts"])
        print(query)
        session.execute(query)
        print("Reading data from kafka topic and write to cassandra done !!!")

    consumer.close()
    cluster.shutdown()

keyspace = "de_pro"
kafka_topic = "tracking"
kafka_bootstrap_servers = "127.0.0.1:9092"
consume_data_from_kafka(keyspace,kafka_topic,kafka_bootstrap_servers)

process = multiprocessing.Process(target=consume_data_from_kafka, args= (keyspace, kafka_topic, kafka_bootstrap_servers))
process.start()
process.join()