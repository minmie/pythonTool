import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!') # exchange为空字符串时，routing_key用来指明朝哪个队列发送消息
print(" [x] Sent 'Hello World!'")
connection.close()