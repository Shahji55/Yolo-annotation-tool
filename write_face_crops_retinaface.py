import cv2 
from retinaface import RetinaFace
import os

# init with normal accuracy option
detector = RetinaFace(quality="high")

def save_face_crops():
    
    images_dir = os.getcwd() + '/images/'
    write_dir = os.getcwd() + '/saved_crops/'

    for file in os.listdir(images_dir):
        image_path = images_dir + file
        image_name = file.split('.')[0]

        orig_image = cv2.imread(image_path)
        # cv2.imwrite(labels_dir + image_name + '.jpg', orig_image)
        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        
        face = detector.predict(image)
        face = sorted(face, key = lambda i: i['x1'])

        if len(face) == 0:
            print("No face found")
            print(image_name)

        elif len(face) > 1:
            print("More than 1 face found")

            for x in range(len(face)):
            
                x1= abs(face[x]["x1"])
                x2= abs(face[x]["x2"])
                y1= abs(face[x]["y1"])
                y2= abs(face[x]["y2"])

                cropped_img = orig_image[y1:y2, x1:x2]
                cv2.imwrite(write_dir + image_name + '_' + str(x) +'.jpg', cropped_img)
       
        else:
            print("1 face found")

            x1= abs(face[0]["x1"])
            x2= abs(face[0]["x2"])
            y1= abs(face[0]["y1"])
            y2= abs(face[0]["y2"])

            cropped_img = orig_image[y1:y2, x1:x2]
            cv2.imwrite(write_dir + image_name + '.jpg', cropped_img)


if __name__ == '__main__':
    save_face_crops()