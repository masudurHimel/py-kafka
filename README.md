# kafka-on-the-go
A repository to test and experiment kafka on the go

**python dependency:** 

`python3 -m venv svenv` \
`source venv/bin/activate`\
`install dependencies: pip install -r requirements.txt`

producer_script run: `python kafka-producer.py`\
consumer_script run: `python kafka-consumer.py <topic name> <consumer group id>`

**Kafka Configure Commands**\
topic_list: `kafka-topics.sh --list --zookeeper zookeeper:2181`\
topic_create: `kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 2 --topic <topic name>`\
topic_delete: `kafka-topics.sh --bootstrap-server kafka:9092 --delete --topic <topic name>`