import pypdf as pdf
from tkinter import *
from tkinter import filedialog, messagebox



def click():
    pass

def pdf_merge():    # merger function
    
    name=str(input("Save merged PDFs as(without extension): "))
    
    to_merge = filedialog.askopenfilenames(
        title="Select PDFs to merge",
        filetypes=[("PDF Files", "*.pdf")])
    
    if not to_merge:
        return
    
    merger = pdf.PdfWriter()
    if len(to_merge)>1:
        for file in to_merge:
            merger.append(file)
        merger.write(f"{name}.pdf")
        merger.close()
    else: 
        print("Cannot merge less than 1 PDF")

window=Tk()
window.geometry("1450x1050") # window size
window.title("PyPDF Editor")
window.config(bg="#076790") #background color

button1=Button(window,text='Merge')
button1.config(command=pdf_merge)
button1.place(x=0,y=0)

window.mainloop()   # creates window