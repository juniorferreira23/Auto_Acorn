import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv
import os
from main import main

load_dotenv()

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


def browse_path(entry):
    path = filedialog.askdirectory() 
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)


def run_interface(app):
    
    def on_start():
        path_input = entry_path1.get()
        path_output = entry_path2.get()
        if not path_input:
            path_input = os.getenv('PATH_INPUTS')
        if not path_output:
            path_output = os.getenv('PATH_OUTPUTS')
        path_output = f'{path_output}/{os.getenv('PATH_OUTPUTS')}'
        messagebox.showinfo('Informação','Iniciando Processo, pode levar alguns minutos dependendo da quantidade de dados de entrada')
        try:
            url = os.getenv('URL')
            main(path_input, path_output, url)
            messagebox.showinfo('Informação','Extração concluída com sucessso')
        except Exception as e:
            messagebox.showinfo(title='Erro', message=e)
        
        
    app.title("Extrator de dados de CNPJ's")
    app.geometry("650x350")

    label_path1 = ctk.CTkLabel(app, text="Selecione a planilha de dados de entrada (Caso a planilha esteja dentro da pasta, não precisa selecionar)")
    label_path1.pack(pady=(20, 5))

    entry_path1 = ctk.CTkEntry(app, width=400)
    entry_path1.pack(pady=5)

    btn_browse1 = ctk.CTkButton(app, text="Selecionar", command=lambda: browse_file(entry_path1))
    btn_browse1.pack(pady=5)

    label_path2 = ctk.CTkLabel(app, text="Destino da Planilha dos dados de saída (Caso deseje salvar dentro da pasta, não precisa selecionar)")
    label_path2.pack(pady=(20, 5))

    entry_path2 = ctk.CTkEntry(app, width=400)
    entry_path2.pack(pady=5)

    btn_browse2 = ctk.CTkButton(app, text="Selecionar", command=lambda: browse_path(entry_path2))
    btn_browse2.pack(pady=5)

    btn_start = ctk.CTkButton(app, text="Iniciar", command=on_start, fg_color='#151', hover_color='#131')
    btn_start.pack(pady=20)


if __name__ == "__main__":
    app = ctk.CTk()
    run_interface(app)
    app.mainloop()