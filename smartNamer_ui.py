import os
from tkinter import Tk, Label, Button, filedialog, Text, Scrollbar, Frame, Entry, BOTH, RIGHT, Y, LEFT
import tkinter as tk

# Import your existing functions
from ai_reader import ai_reader

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Renamer")
        self.root.geometry("400x300")

        # Frame for API key input
        api_frame = Frame(root)
        api_frame.pack(pady=10)

        self.label_api = Label(api_frame, text="API Key:", font=("Helvetica", 12))
        self.label_api.grid(row=0, column=0, padx=5)

        self.entry_api = Entry(api_frame, width=30)
        self.entry_api.grid(row=0, column=1, padx=5)

        # Frame for directory selection
        dir_frame = Frame(root)
        dir_frame.pack(pady=10)

        self.label_dir = Label(dir_frame, text="Select PDF Directory:", font=("Helvetica", 12))
        self.label_dir.grid(row=0, column=0, padx=5)

        self.select_button = Button(dir_frame, text="Select Directory", command=self.select_directory, font=("Helvetica", 10))
        self.select_button.grid(row=0, column=1, padx=5)

        # Frame for running the renamer
        run_frame = Frame(root)
        run_frame.pack(pady=10)

        self.run_button = Button(run_frame, text="Run Renamer", command=self.run_renamer, font=("Helvetica", 10), bg="#4CAF50", fg="white")
        self.run_button.pack()

        # Frame for log text
        log_frame = Frame(root)
        log_frame.pack(pady=10, fill=BOTH, expand=True)

        self.log_text = Text(log_frame, height=10, width=50, wrap='word', font=("Helvetica", 10))
        self.log_text.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(log_frame, command=self.log_text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.log_text.config(yscrollcommand=scrollbar.set)

    def select_directory(self):
        self.pdfs_dir = filedialog.askdirectory()
        self.log("Selected Directory: " + self.pdfs_dir)
    
    def run_renamer(self):
        if hasattr(self, 'pdfs_dir'):
            # Update the directory path in the original script
            os.chdir(self.pdfs_dir)
            ai_reader(self.entry_api.get(), self.pdfs_dir)
            self.log("Renaming Completed")
        else:
            self.log("Please select a directory first")
    
    def log(self, message):
        self.log_text.insert('end', message + '\n')
        self.log_text.see('end')

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
