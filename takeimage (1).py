import cv2
import os
import numpy as np
import shutil

cap = cv2.VideoCapture(0)

def mse(image1, image2):
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err

def compareimages():
    dir1 = 'data1'
    dir2 = 'data2'
    images1 = [os.path.join(dir1, f) for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f)) and f != ".DS_Store"]
    images2 = [os.path.join(dir2, f) for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f)) and f != ".DS_Store"]
    error = 0
    for image1 in images1:
        for image2 in images2:
            img1 = cv2.imread(image1)
            img2 = cv2.imread(image2)
            img1 = cv2.resize(img1, (500, 500))
            img2 = cv2.resize(img2, (500, 500))
            error += mse(img1, img2)
            
    error /= 100
    print(f"Similarity score: {error}")
    reversedata()

def reversedata():
    source_folder = "data2"
    destination_folder = "data1"
    for file in os.listdir(destination_folder):
        file_path = os.path.join(destination_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination_folder)
def takeimages():
    
    dir_path = 'data1'
    for i in range(5):
        ret, frame = cap.read()
        if ret:
            try:
                if not os.listdir(dir_path):
                    cv2.imwrite('data1/frame'+str(i)+'.jpg', frame)
                else:
                    cv2.imwrite('data2/frame'+str(i)+'.jpg', frame)
            except:
                print('Some exception has occurred!')

    compareimages()

takeimages()
