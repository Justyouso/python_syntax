# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-11-29 上午10:57

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

# 声明一个队列(即没有队列创建队列)
channel.queue_declare(queue='my_queue')

# 交换机; 队列名,写明将消息发往哪个队列; 消息内容
# routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列
channel.basic_publish(exchange='', routing_key='hh', body='你好！')

# 关闭链接
connection.close()