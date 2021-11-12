import boto3
import random
import cv2
import os, glob
import csv


BUCKET_NAME = 'lab2-images-hotdog'
#fields = ["image_id","label"]
csv_name = "underbase.csv"
with open(csv_name, 'a', encoding='UTF8', newline='') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.writer(csvfile)
    # writing headers (field names) 
    #writer.writerow(fields)

def download_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    list_images = list(my_bucket.objects.filter(Prefix="underbase")) #my_bucket.objects.all()
    list_4images = random.choices(population=list_images, k=4)
    # download 4 files into current directory
    for item in list_4images:
        filename = item.key
        nom_file = filename.split('/')[-1]
        my_bucket.download_file(filename, nom_file)
        img = cv2.imread(nom_file)
        cv2.imshow(nom_file, img)
        label = cv2.waitKey(0)

        while label != 48 and label != 49: #code ASCII de 0 et 1
            print("Vous ne pouvez étiqueter qu'avec 0 ou 1  !")
            label = cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Ecrire le label dans le csv sur le bucket s3
        with open(csv_name, 'a', encoding='UTF8', newline='') as csvfile: 
            # creating a csv dict writer object 
            writer = csv.writer(csvfile)
            # writing data rows
            label_num = 0 if label == 48 else 1
            row = [nom_file, label_num]
            writer.writerow(row)
    my_bucket.upload_file(csv_name,csv_name)
    print("le fichier csv a été envoyé avec succès")





def upload_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    folder_path=input("Entrez le chemin du dossier/fichiers a upload : ")
    if os.path.isdir(folder_path) :
        for file in glob.glob(os.path.join(folder_path, '*')):
            file_name = file.split('\\')[-1]
            my_bucket.upload_file(file,"underbase/{}".format(file_name))
            print("L'image a été envoyée avec succès")
    elif os.path.isfile:
        my_bucket.upload_file(folder_path,"underbase/{}".format(folder_path))
        print("L'image a été envoyée avec succès")
        

        

print("Si vous voulez labelliser des images, appuyez sur 'L', si vous voulez uploader des images, appuyez sur 'U', si vous voulez quitter, appuyez sur 'Q'. ")
flag = True
while flag :
    x = input("[L/U/Q] ")
    if x =="L" or x=="l":
        download_files()
    elif x=="U" or x=="u":
        upload_files()
    elif x=="Q" or x=="q":
        flag = False