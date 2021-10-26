import cv2 
import os

# Function to get current working directory
def get_cwd():
    cwd = os.getcwd()
    return cwd

# Method to draw bounding boxes on detections for all images in the directory
# and then save results
def draw_bboxes_save_result():
    cwd = get_cwd()
    print(cwd)

    folder_path = cwd + '/images_final_annotations/'

    write_path = cwd + '/saved_results/40_59_new/'

    print(folder_path)

    class_dict = {
        0: '3-12',
        1: '13-19',
        2: '20-39',
        3: '40-59',
        4: '60+'
    }

    color_red = (0, 0, 255) # red
    color_green = (0,255,0) # green
    # color_blue = (255, 0, 0) # blue
    thickness = 2

    for filename in sorted(os.listdir(folder_path)):
        name = filename.split('.')
        print(filename)
        print(name)
        if '.txt' not in filename:
            print("------------------------------------------")
            print("Opening file: ", name[0])
            print("------------------------------------------")
            img = cv2.imread(os.path.join(folder_path, filename))

            dh, dw, _ = img.shape

            file_path = folder_path + name[0] + '.txt'
            print(file_path)
            file = open(file_path, "r+")
            data = file.readlines()
            file.close()

            for line in data:
                class_id, x, y, w, h = map(float, line.split(' '))
                x1, y1, x2, y2 = yolo_bbox_to_bbox(x, y, w, h, dw, dh)

                c1, c2 = (int(x1),int(y1)),(int(x2), int(y2))
                cv2.rectangle(img, c1, c2, color_red , thickness)

                label = class_dict[class_id]
                cv2.putText(img, label, (c1[0], c1[1] - 2), 0, 2 / 3, color_green, thickness, lineType=cv2.LINE_AA)
     
            print("----Writing file-----")        

            file_to_write = write_path + filename
            cv2.imwrite(file_to_write, img)

            print("SUCCESS")
        
        elif '.txt' in filename:
            pass

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

if __name__ == '__main__':
    draw_bboxes_save_result()