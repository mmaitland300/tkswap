from tkinter import *
import PIL.Image as Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import cv2
from main import swap




def select_images():
    # grab a reference to the image panels
    global panelA, panelB, panelC
    # open a file chooser dialog and allow the user to select an input
    # image
    
    path1 = askopenfilename()
    if len(path1) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image1 = cv2.imread(path1)
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image1 = Image.fromarray(image1)
        w, h = image1.size
        ratio = (w // h)
        try:
            image1 = image1.resize(((450), (450*ratio)),Image.ANTIALIAS)
        except ValueError:
            ratio = (h // w)
            image1 = image1.resize(((450 * ratio), (450)),Image.ANTIALIAS)

    	
        # ...and then to ImageTk format
        image1 = ImageTk.PhotoImage(image1)
        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image1)
            panelA.image1 = image1
            panelA.place(relx = 0.0,  
                        rely = 1.0,  
                        anchor ='sw') 
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image1)
            panelA.image1 = image1
    
    path2 = askopenfilename()
    if len(path2) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path2)
        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        image = Image.fromarray(image)
        w, h = image.size
        ratio = (w // h)
        try:
            image = image.resize(((450), (450*ratio)),Image.ANTIALIAS)
        except ValueError:
            ratio = (h // w)
            image = image.resize(((450 * ratio), (450)),Image.ANTIALIAS)
    	
      	# ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelB = Label(image=image)
            panelB.image = image
            panelB.place(relx = 1.0,  
                        rely = 1.0,  
                        anchor ='se') 

        else:
            # update the pannels
            panelB.configure(image=image)
            panelB.image = image
    

        
        img = swap(path1, path2)
        
        # PhotoImage class is used to add image to widgets, icons etc 
        img = ImageTk.PhotoImage(img)
        
            
        # create a label 
        panel = Label(root, image = img, compound=BOTTOM)
        panel.place(relx = 0.5,  
                   rely = 0.0, 
                   anchor = 'n') 
                
        # set the image as img  
        panel.image = img 
        panel.pack(side = "top")





root = Tk()
panelA = None
panelB = None
panelC = None

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn = Button(root, text="Select images", command=select_images)
btn.pack(side="top", expand="yes")





root.geometry("1024x574")
# kick off the GUI
root.mainloop()
