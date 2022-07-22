import hideme
from tkinter import Button, Tk
app = Tk()
app.title("HideMe")
app.geometry("300x100")
openFileBtn = Button(app, text="Open original file", command=hideme.OpenOriginalFile).pack()
openFileToHideBnt = Button(app, text="Open file to hide", command=hideme.OpenFileToHide).pack()
saveModifiedFileBtn = Button(app, text="Save modified file", command=hideme.SaveModifiedFile).pack()
extractHiddenDatBtn = Button(app, text="Extract hidden file", command=hideme.ExtractHiddenData).pack()
app.mainloop()