import json
import random
import sys
from time import sleep

from kafka import KafkaProducer
import itertools


def produceData(topic_list=None, broker_url='localhost:9092'):
    if topic_list is None:
        topic_list = ['defaultTopic']

    producer = KafkaProducer(
        bootstrap_servers=[broker_url],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for topic in itertools.cycle(topic_list):
        print(f"Writing on topic {topic}")
        producer.send(topic, value={f'Hello from topic {topic}': random.randint(0, 1000)})
        sleep(1)


if __name__ == "__main__":
    produceData(topic_list=sys.argv[1:])
