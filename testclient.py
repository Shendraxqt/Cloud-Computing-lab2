#Sending messages to queue (client side)

import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName='lab2', Attributes={'DelaySeconds': '0'})

queueReponse = sqs.create_queue(QueueName='lab2.1', Attributes={'DelaySeconds': '0'})

flag = True
while flag :
    string=""
    print("entrer votre liste de nombres (entre 1 et 10)")
    for i in range(10):
        x=input("Entre le {} ème nombre (pour arretr avant le dernier, faite entrer)".format(i+1))
        if x=="":
            break
        elif not(x.isnumeric()) or int(x)<0:
            print("entre non valide")
            break
        else:
          string = string+x+" "
    response=queue.send_message(MessageBody=string)
    y=input("Voulez-vous envoyé un nouveau message? [Y/n]")
    if y!="Y":
        flag=False


while True:
    for message in queueReponse.receive_messages(MaxNumberOfMessages=10):
        print(message.body)
        message.delete()
