#!/usr/bin/env python
# coding=utf-8
import pika

auth = pika.PlainCredentials('netology', 'netology')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.56.103', credentials=auth))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')
connection.close()