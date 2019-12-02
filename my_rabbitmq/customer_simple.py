# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-12-2 上午10:46

import pika

# 账号信息
username = "wangchao"
pwd = "wangchao520333"

# 生成认证
user_pwd = pika.PlainCredentials(username, pwd)

# rabbitmq服务地址,必须开发5672端口
hostname = '119.3.230.228'

# 连接参数
parameters = pika.ConnectionParameters(hostname, credentials=user_pwd)

# 建立连接
connection = pika.BlockingConnection(parameters)

# 创建通道
channel = connection.channel()

# 声明一个队列(即没有队列创建队列),生产者声明的队列
channel.queue_declare(queue='my_queue')


# 回调函数
def callback(ch, method, properties, body):
    print('body:', body.decode('utf-8'))


# 告诉rabbitmq使用callback来接收信息
channel.basic_consume(queue="hh", on_message_callback=callback,
                      auto_ack=True, )

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
print('等待接收消息......')
channel.start_consuming()
