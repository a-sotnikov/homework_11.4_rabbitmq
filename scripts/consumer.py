#!/usr/bin/env python
# coding=utf-8
import pika

auth = pika.PlainCredentials('netology', 'netology')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.107', credentials=auth))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
#print(dir(channel.basic_consume()))
channel.start_consuming()