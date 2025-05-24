import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, ttk
import threading
import fitz
from highlight_extractor import get_highlighted_annotations
from text_extractor import get_text_annotations
from merge_annotations import merge_annotations
from export_word import export_annotations_to_docx

def run_export_gui():
    def select_pdf():
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            pdf_path.set(file_path)

    def select_output_path():
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
        if file_path:
            output_path.set(file_path)

    def run_export():
        def task():
            try:
                status_label.config(text="Opening PDF...")
                progress_var.set(10)
                doc = fitz.open(pdf_path.get())

                status_label.config(text="Extracting highlighted annotations...")
                progress_var.set(30)
                highlighted_annotations = get_highlighted_annotations(doc)

                status_label.config(text="Extracting text annotations...")
                progress_var.set(50)
                text_annotations = get_text_annotations(doc)

                status_label.config(text="Merging annotations...")
                progress_var.set(70)
                all_annotations = merge_annotations(highlighted_annotations, text_annotations, doc)

                status_label.config(text="Exporting to Word...")
                progress_var.set(90)
                export_annotations_to_docx(title_entry.get(), all_annotations, output_path.get())

                progress_var.set(100)
                status_label.config(text="Done.")
                messagebox.showinfo("Success", "Export completed.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                status_label.config(text="An error occurred.")
            finally:
                export_button.config(state=tk.NORMAL)
                progress_bar.stop()

        if not pdf_path.get() or not output_path.get() or not title_entry.get():
            messagebox.showerror("Error", "Please, fill all the fields.")
            return

        export_button.config(state=tk.DISABLED)
        progress_bar.start()
        threading.Thread(target=task).start()

    # UI setup
    root = tk.Tk()
    root.title("Export PDF Annotations to Word")
    root.geometry("400x300")

    pdf_path = tk.StringVar()
    output_path = tk.StringVar()

    tk.Button(root, text="Select PDF file", command=select_pdf).pack(pady=5)
    tk.Button(root, text="Choose export location", command=select_output_path).pack(pady=5)

    tk.Label(root, text="Document title:").pack()
    title_entry = tk.Entry(root, width=40)
    title_entry.pack(pady=5)

    export_button = tk.Button(root, text="Export", command=run_export)
    export_button.pack(pady=10)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, length=300, variable=progress_var, maximum=100, mode='determinate')
    progress_bar.pack(pady=10)

    status_label = tk.Label(root, text="", fg="gray")
    status_label.pack()

    root.mainloop()