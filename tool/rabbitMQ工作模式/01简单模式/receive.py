#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(method)
    print(method.delivery_tag)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True) # auto_ack=True:T无应答，F有应答

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()