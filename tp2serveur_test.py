import boto3
import statistics

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName='lab2', Attributes={'DelaySeconds': '0'})
messageToSubmit = '5'
response = queue.send_message(MessageBody=messageToSubmit)
messageToSubmit = '4'
response = queue.send_message(MessageBody=messageToSubmit)
messageToSubmit = '6'
response = queue.send_message(MessageBody=messageToSubmit)

for message in queue.receive_messages(MaxNumberOfMessages=10):
    tab=message.body.split()
    tabnum=list(map(int,tab))
    answer ="moyenne : {}, minimum : {}, maximum : {}, median : {}".format(sum(tabnum)/len(tabnum),min(tabnum),max(tabnum),statistics.median(tabnum))
    message.delete()
print(answer)

#send to client

#write log file in SC3