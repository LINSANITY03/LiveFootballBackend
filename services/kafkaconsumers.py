from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('tunnel1',
                         bootstrap_servers=['localhost:9092'],
                         api_version=(0, 10)
                         )


def start_receiver():
    for message in consumer:
        print(json.loads(message.value))
