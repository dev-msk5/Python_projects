import pypdf as pdf
from tkinter import *
from tkinter import filedialog

x_dim="1250"
y_dim="750"
center_x = 625
center_y = 375
offset = 100
name=None

def submit():
    submitted=user_entry.get()

def pdf_merge():    # merger function
    
    to_merge = filedialog.askopenfilenames(
        title="Select PDFs to merge",
        filetypes=[("PDF Files", "*.pdf")])
    
    if not to_merge:
        return
    
    merger = pdf.PdfWriter()
    if len(to_merge)>1 and name!=None:
        for file in to_merge:
            merger.append(file)
        merger.write(f"{name}.pdf")
        merger.close()
    else: 
        print("Cannot merge less than 1 PDF")

window=Tk()         # App container init
window.geometry(f"{x_dim}x{y_dim}") 
window.title("PyPDF Editor")
window.config(bg="#49636E")

default=Frame(window)
page_merge = Frame(window, bg="#BCCF10")
page_cut = Frame(window, bg="#135BB9")          # frames for each action
page_reorder = Frame(window, bg="#2B9976")
page_split = Frame(window, bg="#A54633")

for frame in (default,page_merge, page_cut,page_reorder,page_split):
    frame.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# merge page
Label(page_merge, text="Merge", font=("Arial", 25)).place(x=(int(x_dim)/2)-30, y=100)
Button(page_merge, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
Button(page_merge, text="Select PDFs to merge", command=pdf_merge).place(x=680, y=170)
user_entry = Entry(page_merge)      # field for the user
user_entry.config(font="50")
user_entry.insert(0,"Enter final name")
user_entry.bind("<Return>", lambda event: globals().__setitem__('name', user_entry.get())) # on enter set name = entry text
user_entry.place(x=400, y=170)

# cut page
Label(page_cut, text="Cut", font=("Arial", 25)).place(x=500, y=100)
Button(page_cut, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
user_entry = Entry(page_cut)      # field for the user
user_entry.config(font="50")
user_entry.insert(0,"Enter final name")
user_entry.bind("<Return>", lambda event: globals().__setitem__('name', user_entry.get())) # on enter set name = entry text
user_entry.place(x=400, y=170)


# reorder paeg
Label(page_reorder, text="Reorder", font=("Arial", 25)).place(x=500, y=100)
Button(page_reorder, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
user_entry = Entry(page_reorder)      # field for the user
user_entry.config(font="50")
user_entry.insert(0,"Enter final name")
user_entry.bind("<Return>", lambda event: globals().__setitem__('name', user_entry.get())) # on enter set name = entry text
user_entry.place(x=400, y=170)

# split page
Label(page_split, text="Split", font=("Arial", 25)).place(x=500, y=100)
Button(page_split, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
user_entry = Entry(page_split)      # field for the user
user_entry.config(font="50")
user_entry.insert(0,"Enter final name")
user_entry.bind("<Return>", lambda event: globals().__setitem__('name', user_entry.get())) # on enter set name = entry text
user_entry.place(x=400, y=170)

# default menu
label = Label(default, text="PDF with Python")  # app name
label.config(font='80')
label.place(x=400, y=100)



# navi buttons
Button(default, text="Merge PDFs", command=lambda: page_merge.tkraise()).place(x=center_x - offset, y=center_y - offset)
Button(default, text="Cut PDFs", command=lambda: page_cut.tkraise()).place(x=center_x - offset, y=center_y + offset)
Button(default, text="Reorder PDFs", command=lambda: page_reorder.tkraise()).place(x=center_x + offset, y=center_y - offset)
Button(default, text="Split PDFs", command=lambda: page_split.tkraise()).place(x=center_x + offset, y=center_y + offset)




default.tkraise()  # default to the top level

window.mainloop()   # creates window

# TODO cut pages

# TODO reorder

# TODO split