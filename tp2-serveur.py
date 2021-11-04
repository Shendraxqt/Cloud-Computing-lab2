import boto3
import statistics

sqs = boto3.resource('sqs')
s3 = boto3.resource('s3')

queue = sqs.create_queue(QueueName='lab2', Attributes={'DelaySeconds': '0'})

queueReponse = sqs.create_queue(QueueName='lab2_1', Attributes={'DelaySeconds': '0'})



while(1):
    answer = ""
    for message in queue.receive_messages(MaxNumberOfMessages=10):
        tab=message.body.split()
        tabnum=list(map(int,tab))
        answer ="moyenne : {}, minimum : {}, maximum : {}, median : {}".format(sum(tabnum)/len(tabnum),min(tabnum),max(tabnum),statistics.median(tabnum))
        message.delete()

    #send to client
    if(answer != ""):
        response=queueReponse.send_message(MessageBody=answer)

        #write log file in S3
        with open('logs.txt', 'a') as f:
            for element in tab:
                f.write(element + " ")
            f.write(answer +'\n')
        BUCKET = "lab2-cc-logs"
        s3.Bucket(BUCKET).upload_file("logs.txt", "dump/logs.txt")

