from confluent_kafka import Producer
import json

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

p = Producer({'bootstrap.servers': 'localhost:9092'})
p.produce('user-events', json.dumps({'event': 'signup'}).encode('utf-8'), callback=delivery_report)
p.flush()
