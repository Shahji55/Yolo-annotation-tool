import os
  
def main():
    files_path = os.getcwd() + '/images/'

    for count, file in enumerate(sorted(os.listdir(files_path))):
        if '.jpg' in file:
            dst = "new_data_" + str(count + 4200) + ".jpg"
            # dst = "group_" + str(count + 800) + ".txt"
            src = files_path + file
            dst = files_path + dst

            txt_split = file.split('.')
            #print(txt_split)

            print("Length of txt_split: ", len(txt_split))
            if len(txt_split) == 2:
                src_txt_file = file.split('.')[0] + ".txt"
            
            elif len(txt_split) == 3:
                src_txt_file = txt_split[0] + "." + txt_split[1] + ".txt"

            print(src_txt_file)

            dst_txt = "new_data_" + str(count + 4200) + ".txt"

            src_txt = files_path + src_txt_file
            dst_txt = files_path + dst_txt

            if os.path.exists(src_txt):
                os.rename(src, dst)
                os.rename(src_txt, dst_txt)

def new_rename():
    files_path = os.getcwd() + '/images/'

    for count, file in enumerate(sorted(os.listdir(files_path))):
        if '.jpg' in file:
            dst = "male_" + str(count + 1) + ".jpg"
            src = files_path + file
            dst = files_path + dst

            os.rename(src, dst)
            
  
if __name__ == '__main__':
    main()
    # new_rename()