import pypdf as pdf
from tkinter import *
from tkinter import filedialog,simpledialog

x_dim="1250"
y_dim="750"
center_x = int(x_dim)/2
center_y = int(y_dim)/2
offset = 100
name=None

# def submit():
#     submitted=user_entry.get()

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

def pdf_cut():
    to_cut = filedialog.askopenfilename(
        title="Select PDF to cut pages from",
        filetypes=[("PDF Files", "*.pdf")])

    if not to_cut:
        return

    pages_str = simpledialog.askstring(     # ask user for page numbers to keep (eg. 1,3,5-7)
        "Pages to Keep",
        "Enter page numbers to keep (e.g., 1,3,5-7):",
        parent=window
    )
    if not pages_str:
        return

    def parse_pages(pages_str, num_pages):
        pages = set()
        for part in pages_str.split(','):
            part = part.strip()
            if '-' in part:
                start, end = part.split('-')
                pages.update(range(int(start)-1, int(end)))
            else:
                pages.add(int(part)-1)
                
        return [p for p in sorted(pages) if 0 <= p < num_pages]

    reader = pdf.PdfReader(to_cut)
    num_pages = len(reader.pages)
    keep_pages = parse_pages(pages_str, num_pages)
    if not keep_pages:
        print("No valid pages selected")
        return

    writer = pdf.PdfWriter()
    for i in keep_pages:
        writer.add_page(reader.pages[i])

    out_name = name if name else "cut_output"
    writer.write(f"{out_name}.pdf")
    writer.close()

def pdf_reorder():
    reader = None 
    reorder_window = Toplevel(window)
    reorder_window.title("Reorder PDF Pages")
    reorder_window.geometry("400x500")

    reorder_listbox = Listbox(reorder_window, selectmode=SINGLE, width=30, height=20)
    reorder_listbox.pack(pady=10)

    def load_pdf_for_reorder():
        nonlocal reader
        file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if not file:
            return
        reader = pdf.PdfReader(file)
        reorder_listbox.delete(0, END)
        for i in range(len(reader.pages)):
            reorder_listbox.insert(END, f"Page {i+1}")

    def move_up():                                                  # move page up
        sel = reorder_listbox.curselection()
        if not sel:
            return
        i = sel[0]
        if i > 0:
            text = reorder_listbox.get(i)
            reorder_listbox.delete(i)
            reorder_listbox.insert(i-1, text)
            reorder_listbox.selection_set(i-1)

    def move_down():                                            # move page down
        sel = reorder_listbox.curselection()
        if not sel:
            return
        i = sel[0]
        if i < reorder_listbox.size()-1:
            text = reorder_listbox.get(i)
            reorder_listbox.delete(i)
            reorder_listbox.insert(i+1, text)
            reorder_listbox.selection_set(i+1)
    def save_reordered():                                  # save file as given
        if not reader:
            return
        writer = pdf.PdfWriter()
        order = reorder_listbox.get(0, END)
        for page_text in order:
            page_num = int(page_text.split()[1]) - 1
            writer.add_page(reader.pages[page_num])
        out_name = name if name else "reordered"
        writer.write(f"{out_name}.pdf")
        print(f"Saved as {out_name}.pdf")


    btn_load = Button(reorder_window, text="Load PDF", command=load_pdf_for_reorder)
    btn_load.pack()
    btn_up = Button(reorder_window, text="Move Up", command=move_up)
    btn_up.pack()
    btn_down = Button(reorder_window, text="Move Down", command=move_down)
    btn_down.pack()
    btn_save = Button(reorder_window, text="Save Reordered", command=save_reordered)
    btn_save.pack(pady=10)


def pdf_split(output1="part1.pdf", output2="part2.pdf"):
    
    to_split = filedialog.askopenfilenames(
        title="Select PDF to split",
        filetypes=[("PDF Files", "*.pdf")])
    
    split_at = simpledialog.askstring(     # ask user for page number to split in pop up
    "Split at page",
    "Enter page number to split at:",
    parent=window
)
    if not split_at:
        return

    if not to_split:
        return
    else:
        reader = pdf.PdfReader(to_split[0])
    try:
        split_at_int = int(split_at)
    except ValueError:
        print("Invalid page number for splitting.")
        return

    splitter1 = pdf.PdfWriter()
    for i in range(split_at_int):   # pages 0 .. split_at-1
        splitter1.add_page(reader.pages[i])
    with open(output1, "wb") as f:
        splitter1.write(f)

    splitter2 = pdf.PdfWriter()
    for i in range(split_at_int, len(reader.pages)):  # pages split_at .. end
        splitter2.add_page(reader.pages[i])
    with open(output2, "wb") as f:
        splitter2.write(f)
    
    print(f"PDF split successfully into {output1} and {output2}")

window=Tk()         # App container init
window.geometry(f"{x_dim}x{y_dim}") 
window.title("PyPDF Editor")

default=Frame(window,bg="#3095C0")
page_merge = Frame(window, bg="#008080")
page_cut = Frame(window, bg="#135BB9")          # frames for each action
page_reorder = Frame(window, bg="#136C45")
page_split = Frame(window, bg="#A54633")

for frame in (default,page_merge, page_cut,page_reorder,page_split):
    frame.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# merge page
Label(page_merge, text="Merge", font=("Arial", 25)).place(x=(int(x_dim)/2-100), y=100)
Button(page_merge, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
Button(page_merge, text="Select PDFs to merge", command=pdf_merge).place(x=680, y=170)
user_entry_merge = Entry(page_merge)      # field for the user
user_entry_merge.config(font="50")
user_entry_merge.insert(0,"Enter final name")
user_entry_merge.bind("<Return>", lambda event: globals().__setitem__('name', user_entry_merge.get())) # on enter set name = entry text
user_entry_merge.place(x=400, y=170)

# cut page
Label(page_cut, text="Cut", font=("Arial", 25)).place(x=565, y=100)
Button(page_cut, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
Button(page_cut, text="Select PDFs to cut", command=pdf_cut).place(x=680, y=170)
user_entry_cut = Entry(page_cut)      # field for the user
user_entry_cut.config(font="50")
user_entry_cut.insert(0,"Enter final name")
user_entry_cut.bind("<Return>", lambda event: globals().__setitem__('name', user_entry_cut.get())) # on enter set name = entry text
user_entry_cut.place(x=400, y=170)


# reorder paeg
Label(page_reorder, text="Reorder", font=("Arial", 25)).place(x=500, y=100)
Button(page_reorder, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
Button(page_reorder, text="Select PDFs to reorder", command=pdf_reorder).place(x=680, y=170)
user_entry_reorder = Entry(page_reorder)      # field for the user
user_entry_reorder.config(font="50")
user_entry_reorder.insert(0,"Enter final name")
user_entry_reorder.bind("<Return>", lambda event: globals().__setitem__('name', user_entry_reorder.get())) # on enter set name = entry text
user_entry_reorder.place(x=400, y=170)

# split page
Label(page_split, text="Split", font=("Arial", 25)).place(x=555, y=100)
Button(page_split, text="Go to Menu", command=lambda: default.tkraise()).place(x=50, y=50)
Button(page_split, text="Select PDFs to split", command=pdf_split).place(x=680, y=170)
user_entry_split = Entry(page_split)      # field for the user
user_entry_split.config(font="50")
user_entry_split.insert(0,"Enter final name")
user_entry_split.bind("<Return>", lambda event: globals().__setitem__('name', user_entry_split.get())) # on enter set name = entry text
user_entry_split.place(x=400, y=170)

# default menu
label = Label(default, text="PDF with Python")  # app name
label.config(font='80')
label.place(x=center_x-30, y=center_y-200)



# navi buttons
Button(default, text="Merge PDFs", command=lambda: page_merge.tkraise()).place(x=center_x - offset, y=center_y - offset)
Button(default, text="Cut PDFs", command=lambda: page_cut.tkraise()).place(x=center_x - offset, y=center_y + offset)
Button(default, text="Reorder PDFs", command=lambda: page_reorder.tkraise()).place(x=center_x + offset, y=center_y - offset)
Button(default, text="Split PDFs", command=lambda: page_split.tkraise()).place(x=center_x + offset, y=center_y + offset)




default.tkraise()  # default to the top level

window.mainloop()   # creates window