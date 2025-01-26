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
        path_input = entry_input.get()
        path_output = entry_output.get()
        if not path_input:
            path_input = os.getenv('PATH_INPUTS')
        if not path_output:
            path_output = os.getenv('PATH_OUTPUTS')
        path_output = f'{path_output}/{os.getenv("PATH_OUTPUTS")}'
        
        messagebox.showinfo('Informação', 'Processo iniciado. Pode levar alguns minutos, dependendo do volume de dados.')
        try:
            url = os.getenv('URL')
            main(path_input, path_output, url)
            messagebox.showinfo('Informação', 'Processo concluído com sucesso.')
        except Exception as e:
            messagebox.showerror('Erro', f'Ocorreu um erro durante o processo:\n{e}')
    
    app.title("Extrator de Dados de CNPJs")
    app.geometry("600x350")

    label_input = ctk.CTkLabel(app, text="Selecione o arquivo de entrada (planilha)", font=('Century Gothic bold', 14), )
    label_input.grid(row=0, column=0, sticky='w', padx=20, pady=(10, 0))
    
    span_input = ctk.CTkLabel(app, text="(Se o arquivo estiver no caminho padrão, não é necessário selecionar)", font=('Century Gothic', 12))
    span_input.grid(row=1, column=0, sticky='w', padx=20, pady=(0, 10))

    entry_input = ctk.CTkEntry(app, width=350)
    entry_input.grid(row=2, column=0, sticky='w', padx=(20, 0), pady=(0, 20))

    btn_input = ctk.CTkButton(app, text="Selecionar Arquivo", command=lambda: browse_file(entry_input))
    btn_input.grid(row=2, column=1, sticky='w', padx=(0, 20), pady=(0, 20))

    label_output = ctk.CTkLabel(app, text="Escolha o destino do arquivo de saída", font=('Century Gothic bold', 14))
    label_output.grid(row=3, column=0, sticky='w', padx=20, pady=(0, 0))
    
    span_output = ctk.CTkLabel(app, text="(Se deseja salvar no caminho padrão, não é necessário selecionar)", font=('Century Gothic', 12))
    span_output.grid(row=4, column=0, sticky='w', padx=20, pady=(0, 10))

    entry_output = ctk.CTkEntry(app, width=350)
    entry_output.grid(row=5, column=0, sticky='w', padx=(20, 0), pady=(0, 40))

    btn_output = ctk.CTkButton(app, text="Selecionar Pasta", command=lambda: browse_path(entry_output))
    btn_output.grid(row=5, column=1, sticky='w', padx=(0, 20), pady=(0, 40))

    btn_start = ctk.CTkButton(app, text="Iniciar Processo", command=on_start, fg_color='#151', hover_color='green')
    btn_start.grid(row=6, column=0, sticky='w', padx=20, pady=(0, 10))


if __name__ == "__main__":
    app = ctk.CTk()
    run_interface(app)
    app.mainloop()
