import os
import cv2
import argparse
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from face_detector import select_face
from face_swap import face_swap



def swap(src, dst):
    parser = argparse.ArgumentParser(description='FaceSwapApp')
    parser.add_argument('--warp_2d', default=True, action='store_true', help='2d or 3d warp')
    parser.add_argument('--correct_color', default=True, action='store_true', help='Correct color')
    parser.add_argument('--no_debug_window', default=True, action='store_true', help='Don\'t show debug window')
    args = parser.parse_args()

    # Read images
    src_img = cv2.imread(src)
    dst_img = cv2.imread(dst)
    out = 'imgs/result.jpg'
    # Select src face
    src_points, src_shape, src_face = select_face(src_img)
    # Select dst face
    dst_points, dst_shape, dst_face = select_face(dst_img)

    if src_points is None or dst_points is None:
        print('Detect 0 Face !!!')
        exit(-1)

    output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, dst_img, args)

    dir_path = os.path.dirname(out)
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    cv2.imwrite(out, output)

    im_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(im_rgb)
    
    w, h = image.size
    ratio = (h // w)
         # resize the image and apply a high-quality down sampling filter 
    try:
        image = image.resize(((450), (450*ratio)),Image.ANTIALIAS)
    except ValueError:
        ratio = (w // h)
        image = image.resize(((450 * ratio), (450)),Image.ANTIALIAS)

    return image



# src = "imgs/example6.jpg"
# dst = "imgs/target.png"


# def swap():
#     file1 = askopenfilename(initialdir=os.getcwd(),title="Select Image",
#                                               filetypes=[("Images","*.*")])
    
#     file2 = askopenfilename(initialdir=os.getcwd(),title="Select Image",
#                                               filetypes=[("Images","*.*")])
    
#     x = swap(file1, file2)
#     im_rgb = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
#     image = Image.fromarray(im_rgb)
    
#     w, h = image.size
#     ratio = (h // w)
#         # resize the image and apply a high-quality down sampling filter 
#     try:
#         image = image.resize(((450), (450*ratio)),Image.ANTIALIAS)
#     except ValueError:
#         ratio = (w // h)
#         image = image.resize(((450 * ratio), (450)),Image.ANTIALIAS)

#     # PhotoImage class is used to add image to widgets, icons etc 
#     img = ImageTk.PhotoImage(image)
 
    
#     # create a label 
#     panel = Label(root, image = img, compound=BOTTOM)
        
#     # set the image as img  
#     panel.image = img 
#     panel.pack(side = "bottom")

# root = Tk()

# btn3 = Button(root, text="Swap!", command=swap)
# btn3.pack(side="top", expand="yes")
# root.geometry("1024x574")
# # kick off the GUI
# root.mainloop()
