#!coding=utf-8
''' rabbitmq 服务器'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # declaring the queue

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    ''' slowest recursive implementation possible...'''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def on_request(ch, method, props, body):
    ''' a callback for "basic_consume", the core of RPC Server, and is executed when a request is received'''
    n = int(body)

    print "[.] fib(%s)"%n

    response = fib(n)
    ch.basic_publish(exchange = '', routing_key=props.reply_to, \
                    properties= pika.BasicProperties(correlation_id= props.correlation_id), \
                    body = str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)     # we may want to run more than one server process, in order to spread the load equally over multiple servers, we need to set the prefecth_count to 1.
channel.basic_consume(on_request, queue = 'rpc_queue')

print '[x] Awaiting RPC requests'
channel.start_consuming()