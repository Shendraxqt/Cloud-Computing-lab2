import boto3
import random
import cv2

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


print("Si vous voulez labelliser des images, appuyez sur 'L', si vous voulez uploader des images, appuyez sur 'U', si vous voulez quitter, appuyez sur 'Q'. ")
flag = True
while flag :
    x = input("[L/U/Q]")
    if x =="L" or x=="l":
        download_files()
        flag = False
    elif x=="U" or x=="u":
        # to add
        print("not implemented yet")
        flag = False
    elif x=="Q" or x=="q":
        flag = False
