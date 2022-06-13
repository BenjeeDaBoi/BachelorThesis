import cv2

img = cv2.imread('./testImage.png')

def __showImage__(title, image):
    cv2.imshow(title, image)

def __simpleBWErosion(image):
    
    __showImage__('Raw Image', image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    __showImage__('Grayscale Image', image)
    #image = cv2.equalizeHist(image)
    #(thresh, image) = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)
    #__showImage__('Black & White Image', image)
  
    cv2.imwrite('../source.PNG', image) 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

__simpleBWErosion(img)

# TODO: Research MorphologyEx Methods to extract the egg even better?
