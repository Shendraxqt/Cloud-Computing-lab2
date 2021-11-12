import boto3
import random
import cv2
import os, glob


BUCKET_NAME = 'lab2-images-hotdog2'

def download_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    list_images = list(my_bucket.objects.filter(Prefix="underbase/"))
    list_4images = random.choices(population=list_images, k=4)
    # download 4 files into current directory
    for item in list_4images:
        filename = item.key
        my_bucket.download_file(filename, filename)
        img = cv2.imread(filename)
        cv2.imshow(filename, img)
        label = cv2.waitKey(0)
        #TODO : ecrire le label dans le csv sur le bucket s3
        while label != 48 and label != 49: #code ASCII de 0 et 1
            print("Vous ne pouvez étiqueter qu'avec 0 ou 1  !")
            label = cv2.waitKey(0)
        cv2.destroyAllWindows()

def upload_files():
    s3 = boto3.resource('s3')
    # select bucket
    my_bucket = s3.Bucket(BUCKET_NAME)
    folder_path=input("Entrez le chemin du dossier/fichiers a upload : ")
    if os.path.isdir(folder_path) :
        for file in glob.glob(os.path.join(folder_path, '*')):
            my_bucket.upload_file(file,"underbase/{}.jpg".format(file))
    elif os.path.isfile:
        my_bucket.upload_file(folder_path,"underbase/{}.jpg".format(folder_path))
        

        

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
