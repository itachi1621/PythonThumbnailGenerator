from PIL import Image;
import os;

#Check if thumbnails directory exsists
if not os.path.exists('thumbnails'):
    os.makedirs('thumbnails');

def createThumbnails(image_list,width=128,height=128):
    for image in image_list:
        im = Image.open(image);
        im.thumbnail((width,height));
        im.save('thumbnails/'+image);
        
def findImages(path):
    image_list = [];
    image_type_list = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('.jpg'):
                image_list.append(file);
    return image_list;
        
img_list=["sample.jpg"]



createThumbnails(img_list);
