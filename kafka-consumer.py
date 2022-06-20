import json

from kafka import KafkaConsumer
import sys


def consumeData(topic='testTopic', group_id='test_group', connection_timeout_ms=-1):
    consumer = KafkaConsumer(
        topic, group_id=group_id,
        bootstrap_servers=['localhost:9092'],
        consumer_timeout_ms=connection_timeout_ms,
        auto_offset_reset='latest',
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    for msg in consumer:
        print(msg.value)


if __name__ == "__main__":
    consumeData(topic=sys.argv[1], group_id=sys.argv[2])
