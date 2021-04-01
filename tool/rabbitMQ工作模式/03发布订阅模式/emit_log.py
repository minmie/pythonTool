#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明交换机
channel.exchange_declare(exchange='logs',  # 交换机名称
                         exchange_type='fanout'  # 交换机类型,fanout：发布订阅模式
                         )

message = b' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)  # exchange:要发送到哪个交换机
print(" [x] Sent %r" % message)
connection.close()