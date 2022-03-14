# consumer.py
# Consume RabbitMQ queue

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.1.99', 5672, '/Jcaldwell', pika.PlainCredentials("Jcaldwell", "Jcaldwell")))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(f'{body} is received')


channel.basic_consume(queue="name", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
