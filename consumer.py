from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'analytics-consumer-group',
    'auto.offset.reset': 'earliest'
})
c.subscribe(['user-events'])
