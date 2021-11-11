import boto3
import random
import cv2
from pathlib import Path

BUCKET_NAME = 'lab2-images-hotdog'

def download_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    list_images = list(my_bucket.objects.all())
    list_4images = random.choices(population=list_images, k=4)
    # download 4 files into current directory
    for item in list_4images:
        filename = item.key
        my_bucket.download_file(filename, filename)
        img = cv2.imread(filename)
        cv2.imshow(filename, img)
        label = cv2.waitKey(0)
        while label != 48 and label != 49: #code ASCII de 0 et 1
            print("Vous ne pouvez étiqueter qu'avec 0 ou 1  !")
            label = cv2.waitKey(0)
        cv2.destroyAllWindows()

def upload_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    file_path = input("Entrez le chemin de l'image à upload")//new
    my_bucket.upload_file(file_path,"hotdog.jpg")//changer file_path a la place de "ImagesUpload/hotdog_dog.jpg"
    x=input("Voulez vous uploader une autre image? [Y/n]")//new
    if(x =='Y' or x =='y'))://new//new
        upload_files()//new
    

print("Si vous voulez labelliser des images, appuyez sur 'L', si vous voulez uploader des images, appuyez sur 'U', si vous voulez quitter, appuyez sur 'Q'. ")
flag = True
while flag :
    x = input("[L/U/Q]")
    if x =="L" or x=="l":
        download_files()
        flag = False
    elif x=="U" or x=="u":
        # to add
        upload_files()
        flag = False
    elif x=="Q" or x=="q":
        flag = False
