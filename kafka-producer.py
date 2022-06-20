import json
import random
from time import sleep

from kafka import KafkaProducer
import itertools


def produceData(topic_list):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for topic in itertools.cycle(topic_list):
        producer.send(topic, value={f'Hello from topic {topic}': random.randint(0, 1000)})
        sleep(2)


if __name__ == "__main__":
    produceData(topic_list=['testTopic', 'secondaryTopic'])
