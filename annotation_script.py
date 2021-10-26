import cv2 
import os

def read_existing_annotations():
    images_dir = os.getcwd() + '/images/'
    labels_dir = os.getcwd() + '/annotations/'
    write_dir = os.getcwd() + '/final_annotations/'

    # 3-12, 13-19, 20-39, 40-59, 60+
    class_list = ['0', '1', '2', '3', '4']
    cls = None
    val = 0

    color_red = (0, 0, 255) # red
    thickness = 2

    for file in os.listdir(images_dir):
        image_path = images_dir + file
        image_name = file.split('.')[0]

        orig_image = cv2.imread(image_path)
        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        
        dh, dw, _ = orig_image.shape

        text_file_to_open = labels_dir + image_name + '.txt'
        print(text_file_to_open)
        text_open = open(text_file_to_open, 'r')
        lines = text_open.readlines()

        file_to_write = write_dir + image_name + '.txt'
        file_write = open(file_to_write, 'w')
        
        for line in lines:
            x, y, w, h = map(float, line.split(' '))
            x1, y1, x2, y2 = yolo_bbox_to_bbox(x, y, w, h, dw, dh)

            image_cpy = image.copy()
            cv2.rectangle(image_cpy, (int(x1), int(y1)), (int(x2), int(y2)), color_red, thickness)
            cv2.imshow('image', image_cpy)

            key = cv2.waitKey(0) & 0xFF

            if key == ord('z'):
                val = '0'
            elif key == ord('x'):
                val = '1'
            elif key == ord('c'):
                val = '2'
            elif key == ord('v'):
                val = '3'
            elif key == ord('b'):
                val = '4'
            elif key == ord('s'):
                continue
            elif key == 27:
                break

            if val in class_list:
                cls = str(val)
        
                writeSting = cls +" "+ str(x) + " " + str(y) + " " + str(w) + " " + str(h) +"\n"
                file_write.write(writeSting)
      
 # Function to convert yolo bbox coordinates into opencv format
def yolo_bbox_to_bbox(x, y, w, h, dw, dh):
    x1 = int((x-w/2) * dw)
    y1 = int((y-h/2) * dh)
    x2 = int((x+w/2) * dw)
    y2 = int((y+h/2) * dh)

    if x1 < 0:
        x1 = 0
    if y1 > dw - 1:
        y1 = dw - 1
    if x2 < 0:
        x2 = 0
    if y2 > dh - 1:
        y2 = dh - 1

    return x1, y1, x2, y2

def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)           
        
if __name__ == '__main__':
    read_existing_annotations()