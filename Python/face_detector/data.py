import zipfile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

def imageReadText(img):
    return pytesseract.image_to_string(img).lower().split()
print(text)

def faceFinder(img_path, full_image):
    img = cv.imread(img_path)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.35)
    
    return_list = []
    
    for face in faces:
        tup = (face[0],face[1],face[0]+face[2], face[1]+face[3])
        return_list.append(full_image.crop(tup))
    
    return return_list

def contactSheetConstructor(img_lst):
    import math

    first_image=img_lst[0]
    contact_sheet=Image.new(first_image.mode, (1000, 200 * math.ceil(len(img_lst)/5)))
    
    x=0
    y=0
    for img in img_lst:
        contact_sheet.paste(img, (x, y))
        if x+200 == contact_sheet.width:
            x=0
            y=y+200
        else:
            x=x+200
        
    return contact_sheet

Image_list = []

print("Creating zip instance...")
zip = zipfile.ZipFile('readonly/small_img.zip')
print("Zip instance created. Loading image files...")

for i in zip.infolist():
    
    
    print("Opening file {}...".format(i.filename))
    image_full = Image.open(zip.open(i))
    
    print("Creating dictionary for file {}...".format(i.filename))
    img_dict = {'name':i.filename}
    
    print("Searching file {} for text...".format(i.filename))
    img_dict['text'] = imageReadText(image_full)
    
    print("Text loading complete. Searching file {} for images...".format(i.filename))
    img_dict['faces'] = faceFinder(zip.extract(i), image_full)
    
    print("Face search complete. Inserting results for file {} into the dictionary...".format(i.filename))
    Image_list.append(img_dict)
    
    print("Continuing to next file...")
    
print("Loading complete. Closing zip file.")    
zip.close()

text = ""
print("Beginning word search program")
text = input("Enter a keyword to search for (enter \"exit\" to close: ")

while text.lower() != "exit":
    print("Searching for {}".format(text))
    text = text.lower()

    for img in Image_list:
        if text in img['text']:
            print("Results found in {}".format(img['name']))
        
            if len(img['faces']) == 0: print("But there were not faces in that file!")
            else: display(contactSheetConstructor(img['faces']))
                
    print("Search complete.")
    
    text = input("Enter a keyword to search for (enter \"exit\" to close: ")
    
print("Program exiting")        
