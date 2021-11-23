import cv2 
from retinaface import RetinaFace
import os

# init with normal accuracy option
detector = RetinaFace(quality="high")

def detect_faces_and_write_annotation_file():
    
    # images_dir = os.getcwd() + '/latest/company_vids/test-images/'
    # labels_dir = os.getcwd() + '/latest/company_vids/test-annotations/'

    images_dir = os.getcwd() + '/latest/group_all/images/'
    labels_dir = os.getcwd() + '/latest/group_all/annotations/'

    for file in os.listdir(images_dir):
        image_path = images_dir + file
        image_name = file.split('.')[0]

        print("---------- Opening image: ", image_name)

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
                # print(x)

                with open(labels_dir + image_name + '.txt', 'a') as f:
                    x1= abs(face[x]["x1"])
                    x2= abs(face[x]["x2"])
                    y1= abs(face[x]["y1"])
                    y2= abs(face[x]["y2"])

                    w= x2-x1
                    h= y2-y1

                    x= x1 + (w/2)
                    y= y1 + (h/2)
                    x = x/image.shape[1]
                    y= y/image.shape[0]
                    w = w/image.shape[1]
                    h= h/image.shape[0]

                    writeSting = str(x) + " " + str(y) + " " + str(w) + " " + str(h) +"\n"
                    f.write(writeSting)
        
        else:
            print("1 face found")

            with open(labels_dir + image_name + '.txt', 'w') as f:
                x1= abs(face[0]["x1"])
                x2= abs(face[0]["x2"])
                y1= abs(face[0]["y1"])
                y2= abs(face[0]["y2"])

                w= x2-x1
                h= y2-y1

                x= x1 + (w/2)
                y= y1 + (h/2)
                x = x/image.shape[1]
                y= y/image.shape[0]
                w = w/image.shape[1]
                h= h/image.shape[0]

                writeSting = str(x) + " " + str(y) + " " + str(w) + " " + str(h) +"\n"
                f.write(writeSting)


if __name__ == '__main__':
    detect_faces_and_write_annotation_file()