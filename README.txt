- Original images should be in the 'images' folder.

- Annotation text files without class id are in the 'annotations' folder.

- Run the script using the command 'python annotation_script.py' or just double click on the file 'annotation_script.py'.

- New annotation text files with class id are saved in the 'final_annotations' folder. 

- To verify the annotations, put the original images and their corresponding final annotation text files in the folder 'images_final_annotations'.
Then run the script using the command 'python draw_bboxes.py' or just double click on the file 'draw_bboxes.py'. The results are saved
in the 'saved_results' folder.


Classes:

3-12 = 0 (key = Z)

13-19 = 1 (key = X)

20-39 = 2 (key = C)

40-59 = 3 (key = V)

60+ = 4 (key = B)


ESC key = exit program

'S' key = skip face annotation
