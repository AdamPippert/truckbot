import json
from kafka import KafkaProducer
producer =KafkaProducer(bootstrap_servers='xxx.xxx.xxx.xxx')
filename = truckqueue.json

with open(filename) as f:
        data = json.load(f)
            producer.send_message(topic, data.encode('utf-8')

