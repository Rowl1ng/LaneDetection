import cv2
import numpy as np
import glob
import string
import PolygonFitting as polygon
#from operator import pos
#import Normal as norm
from PIL import Image
from matplotlib import pyplot as plt


def processLightLane(indir,outdir):
    light=147
    print indir
    for image in  glob.glob(indir+'/*.jpg'):
        gray = cv2.imread(image,0)
        cv2.bilateralFilter(gray,9, 90,16)
        img = cv2.GaussianBlur(gray,(7,7),0)
        ret,binimg = cv2.threshold(img,light,255,cv2.THRESH_BINARY)
            
        outfile=str(image).split('\\')[1]
        outfile=outfile.split('.')[0]
        cv2.imwrite(outdir+'/'+outfile+'.jpg',binimg)
            
def processDarkLane(indir,outdir):
    dark=93
    print indir
    #indir1=str(indir)+'/'
    for image in  glob.glob(indir+'/*.jpg'):
        gray = cv2.imread(image,0)
        cv2.bilateralFilter(gray,9, 90,16)
        img = cv2.GaussianBlur(gray,(7,7),0)
        ret,binimg = cv2.threshold(img,dark,255,cv2.THRESH_BINARY)
        outfile=str(image).split('\\')[1]
        outfile=outfile.split('.')[0]
        cv2.imwrite(outdir+'/'+outfile+'.jpg',binimg)
'''def processImage(self,image):
        cv2.bilateralFilter(image, self.thrs1*2+1, 90,16)
        #img = cv2.GaussianBlur(image,(7,7),0)
        
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        #cl1 = clahe.apply(img)
        
        #equ = cv2.equalizeHist(img)
        #res = np.hstack((cl1,image)) #stacking images side-by-side
        #image = np.array(Image.open(filename).convert('L')) 
'''
       # a = np.array(img)
       
 
'''      
 #n=norm.GetAverage(a)
        #u=norm.GetVar(n, a)
        #b=norm.AutoNorm(a)
        
        #b=normalize(a)
        #image= Image.fromarray(b)
        #ret,th1 = cv2.threshold(image,93,255,cv2.THRESH_BINARY)
        return image

def nothing(*arg):
    pass 

def normalize(arr):
    for i in range(3):
        minval = arr[..., i].min()
        maxval = arr[..., i].max()

        if minval != maxval:
            arr[..., i] -= minval
            arr[..., i] *= (255.0 / (maxval - minval))
    return arr



if __name__ == '__main__':
    #fillDet=fill()
    gray = cv2.imread('G:/C/LaneDetection/photos/test/S229A-053+251930-053+247835.jpg',0)
    cv2.bilateralFilter(gray, 51, 90,16)
    

    cv2.namedWindow('fill',0)
    
    cv2.createTrackbar('thrs1', 'fill', 4, 40, nothing)
        
    while True:
        val = cv2.getTrackbarPos('thrs1', 'fill')
        #image=cv2.bilateralFilter(img, val*2+1, 90,16)
        #image=fillDet.processImage(img)
        #res = np.hstack((img,image)) 
        #cv2.imshow('fill', image)
        ch = cv2.waitKey(5)
        if ch==27:
            break
        
    cv2.destroyAllWindows()
    
    print("Testfunction for Filling")

'''



