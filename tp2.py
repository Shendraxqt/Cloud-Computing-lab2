import boto3

sqs = boto3.resource('sqs')

for mesqueue in sqs.queues.all():
   if mesqueue.url == "https://queue.amazonaws.com/706109239716/lab2":
       queue = sqs.get_queue_by_name(QueueName='lab2')
else :
        queue = sqs.create_queue(QueueName='lab2', Attributes={'DelaySeconds': '0'})


string=""
print("entrer votre liste de nombres (entre 1 et 10)")
for i in range(10):
    x=input("Entre le {} ème nombre (pour arretr avant le dernier, faite entrer)".format(i+1))
    if x=="":
        break
    elif not(x.isnumeric()):
        print("entre non valide")
        break
    else:
        string = string+x+" "

response=queue.send_message(MessageBody=string)

for message in queue.receive_messages(MaxNumberOfMessages=10):
    tab=message.body.split()
    tabnum=list(map(int,tab))
    print("moyenne :", sum(tabnum)/len(tabnum), " minimum :", min(tabnum), " maximum :", max(tabnum))
    print(tabnum)
    message.delete()


