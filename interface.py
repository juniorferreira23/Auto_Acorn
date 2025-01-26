import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv
import threading
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

def show_loading():
    loading_window = ctk.CTkToplevel()
    loading_window.title("Processando")
    loading_window.geometry("300x100")
    loading_window.resizable(False, False)
    loading_window.grab_set()  # Impede interação com a janela principal enquanto processa

    label = ctk.CTkLabel(loading_window, text="Processando, aguarde...", font=('Century Gothic bold', 14))
    label.pack(pady=20)

    return loading_window

def run_process(entry_input, entry_output, loading_window):
    try:
        path_input = entry_input.get()
        path_output = entry_output.get()
        if not path_input:
            path_input = os.getenv('PATH_INPUTS')
        if not path_output:
            path_output = os.getenv('PATH_OUTPUTS')
        path_output = f'{path_output}/{os.getenv("PATH_OUTPUTS")}'

        url = os.getenv('URL')
        main(path_input, path_output, url)

        messagebox.showinfo('Informação', 'Processo concluído com sucesso.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro durante o processo:\n{e}')
    finally:
        loading_window.destroy()

def on_start(entry_input, entry_output):
    loading_window = show_loading()
    process_thread = threading.Thread(target=run_process, args=(entry_input, entry_output, loading_window))
    process_thread.start()

def run_interface(app):
    app.title("Extrator de Dados de CNPJs")
    app.geometry("600x350")

    label_input = ctk.CTkLabel(app, text="Selecione o arquivo de entrada (planilha)", font=('Century Gothic bold', 14))
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

    btn_start = ctk.CTkButton(app, text="Iniciar Processo", command=lambda: on_start(entry_input, entry_output), fg_color='#151', hover_color='green')
    btn_start.grid(row=6, column=0, sticky='w', padx=20, pady=(0, 10))

if __name__ == "__main__":
    app = ctk.CTk()
    run_interface(app)
    app.mainloop()