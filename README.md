# Py-Kafka
A repository to test and experiment kafka on the go

## python dependency
```bash
python3 -m venv svenv
source venv/bin/activate
install dependencies: pip install -r requirements.txt
```

## producer_script run
```bash
python kafka-producer.py topic1 topic2
python kafka-producer.py <topic name> <topic name> <topic name>...
```

## consumer_script run
```bash
python kafka-consumer.py <topic name> <consumer group id>
```

## Kafka initialization:
```bash
make kafka
make clean
```

## Kafka shell
**To enter docker shell**
```bash
docker exec -it kafka /bin/sh
```

**To Add/Alter Topic/Partition:**
```bash
kafka-topics.sh --alter --zookeeper zookeeper:2181 --partitions 2 --topic <topic name>
```

**To delete topic:**
```bash
kafka-topics.sh --bootstrap-server kafka:9092 --delete --topic <topic name>
```

**List of topic**
```bash
kafka-topics.sh --list --zookeeper zookeeper:2181
```

**List of messages:**
```bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic name> --from-beginning
```