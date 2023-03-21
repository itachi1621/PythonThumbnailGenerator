from PIL import Image;
import os;
import argparse;

#Check if thumbnails directory exsists

def outputDirectoryCheck(path):
    if not os.path.exists(path):
        os.makedirs(path);
    else:
        pass;
        #print("Directory already exsists");
    


def createThumbnails(image_list,thumbnail_path='thumbnails',width=200,height=200):
    outputDirectoryCheck(thumbnail_path);
    imgamount=str(len(image_list))
    for image in image_list:
        im = Image.open(image);
        im.thumbnail((width,height));
        #get image name for placement in the thumbnail directory
        image_name=os.path.basename(image)
        im.save(os.path.join(thumbnail_path,image_name));
        print('Created thumbnail for '+image_name+' '+str(image_list.index(image)+1)+'/'+imgamount);
        # might modify this to be user defined later or default to thumbnails
        
def findAllImages(path):#Finds all supported images in a given directory including subfolders
    image_list = [];

    pillow_exts = Image.registered_extensions()#Provides a list that pillow supports
    supported_extensions = {ex for ex, f in pillow_exts.items() if f in Image.OPEN}#Filter down list to those who have open feature 
    #print(supported_extensions);
    for root, dirs, files in os.walk(path):
        for file in files:
            #Check if current file ends with a supported extension
            if file.endswith(tuple(supported_extensions)):#Only accept files with supported extensions
                image_list.append(os.path.join(root,file));
            
    return image_list;

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create thumbnails for images in a directory.')
    parser.add_argument('input_dir', help='Input directory containing images to be used for thumbnails')
    parser.add_argument('output_dir', help='Output directory for thumbnails to be placed')
    parser.add_argument('--width', type=int, default=200, help='Width of the thumbnail')
    parser.add_argument('--height', type=int, default=200, help='Height of the thumbnail')

    args=parser.parse_args()

    img_list = findAllImages(args.input_dir);
    print('Found '+str(len(img_list))+' images')
    #print('Found '.len(img_list) + ' images ');
    createThumbnails(img_list,args.output_dir,args.width,args.height);
