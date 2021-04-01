#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 申明交换机
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 声明队列
result = channel.queue_declare(queue='', exclusive=True) # 不指定对列表，系统会自己给队列命名
queue_name = result.method.queue  # 获取队列名称

# 将队列和交换机进行绑定
channel.queue_bind(exchange='logs', queue=queue_name) # exchange:要绑定的交换机名称

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()