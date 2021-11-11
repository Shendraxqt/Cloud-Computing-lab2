import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName='lab2', Attributes={'DelaySeconds': '0'})

queueReponse = sqs.create_queue(QueueName='lab2_1', Attributes={'DelaySeconds': '0'})

# Sending messages to queue
flag = True
while flag :
    string=""
    print("entrez votre liste de nombres (entre 1 et 10 nombres)")
    for i in range(10):
        x=input("Entrez le {} ème nombre (pour arreter avant le dernier, faites entrer)".format(i+1))
        if x=="":
            break
        elif not(x.isnumeric()) or int(x)<0:
            print("entree non valide")
        else:
          string = string+x+" "
    response=queue.send_message(MessageBody=string)
    y=input("Voulez-vous envoyer un nouveau message? [Y/n]")
    if(not(y =='Y' or y =='y')):
        flag=False
        

# Receiving messages and printing them
while True:
    for message in queueReponse.receive_messages(MaxNumberOfMessages=10):
        print(message.body)
        message.delete()
