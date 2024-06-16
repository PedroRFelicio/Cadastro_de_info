import tkinter as tk
from tkinter import ttk 
import mysql.connector 
from tkinter import messagebox 

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pedro1423",
        database="veterinario"
) 

def verificar_usuario_existente(usuario): 
    cursor = conn.cursor()
    comando_select = "SELECT * FROM cadastro WHERE usuario = %s"
    cursor.execute(comando_select, (usuario,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado is not None

def submit_cadastro():
    usuario = entry_usuario.get()
    senha = entry_senha.get() 

    if not usuario or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return
    
    if verificar_usuario_existente(usuario):
        messagebox.showerror("Erro", "Usuário já cadastrado.")
        return
    
    cursor1 = conn.cursor() 
    comando_insert1 = "INSERT INTO cadastro (usuario, senha) VALUES(%s,%s)" 
    valores = (usuario, senha) 

    cursor1.execute(comando_insert1, valores) 
    conn.commit()
    
    cursor1.close()

    cadastros.destroy()
    
    confirma_cadastro()

def confirma_cadastro():
    confirma_window = tk.Toplevel()
    confirma_window.title("Confirmação")

    label = tk.Label(confirma_window, text="Cadastro Confirmado")
    label.pack(pady=20)

    botao_fechar = tk.Button(confirma_window, text="Fechar", command=confirma_window.destroy)
    botao_fechar.pack()

def fazer_login():
    usuario = entry_usuario_login.get()
    senha = entry_senha_login.get()

    if not usuario or not senha:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return 
    
    cursor = conn.cursor()

    comando_select = "SELECT * FROM cadastro WHERE usuario = %s AND senha = %s"
    cursor.execute(comando_select, (usuario, senha))
    resultado = cursor.fetchone()

    cursor.close()

    if resultado:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        
        login_window.destroy()
    else:
        messagebox.showerror("Erro", "Credenciais incorretas.")

def enviar_info():
    nome = entry_nome.get()
    nome_animal = entry_nome_cachorro.get()
    raca = entry_raca.get()
    idade = entry_idade.get()
    telefone = entry_telefone.get()

    cursor = conn.cursor()
    comando_insert = "INSERT INTO Clientes (nome, nome_animal, raca, idade, telefone) VALUES (%s, %s, %s,%s,%s)"
    valores = (nome, nome_animal, raca, idade, telefone) 
    
    cursor.execute(comando_insert, valores)
    conn.commit()
    cursor.close()

    root.destroy()

   
    confirma_info()

def confirma_info():
    confirma_window = tk.Tk()
    confirma_window.title("Confirmação")

    label = tk.Label(confirma_window, text="Cadastro de Informações Bem-Sucedido")
    label.pack(pady=20)

    botao_fechar = tk.Button(confirma_window, text="Fechar", command=lambda: encerrar_programa(confirma_window))
    botao_fechar.pack()

def encerrar_programa(window):
    conn.close()  
    window.destroy()
    exit()


cadastros = tk.Tk()
cadastros.title("Cadastro de Login")

frame = ttk.Frame(cadastros, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S)) 

label_usuario = ttk.Label(frame, text="Usuário:")
label_usuario.grid(column=0, row=0, sticky=tk.W)

entry_usuario = ttk.Entry(frame, width=30)
entry_usuario.grid(column=1, row=0)

label_senha = ttk.Label(frame, text="Senha:")
label_senha.grid(column=0, row=1, sticky=tk.W) 

entry_senha = ttk.Entry(frame, width=30, show="*")
entry_senha.grid(column=1, row=1)

submit_button = ttk.Button(frame, text="Cadastrar", command=submit_cadastro)
submit_button.grid(column=0, row=5, columnspan=2) 

cadastros.mainloop() 


login_window = tk.Tk()
login_window.title("Login")

frame_login = ttk.Frame(login_window, padding="20")
frame_login.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_usuario_login = ttk.Label(frame_login, text="Usuário:")
label_usuario_login.grid(column=0, row=0, sticky=tk.W)

entry_usuario_login = ttk.Entry(frame_login, width=30)
entry_usuario_login.grid(column=1, row=0)

label_senha_login = ttk.Label(frame_login, text="Senha:")
label_senha_login.grid(column=0, row=1, sticky=tk.W)

entry_senha_login = ttk.Entry(frame_login, width=30, show="*")
entry_senha_login.grid(column=1, row=1)

login_button = ttk.Button(frame_login, text="Login", command=fazer_login)
login_button.grid(column=0, row=5, columnspan=2)

login_window.mainloop()


root = tk.Tk()
root.title("Cadastro de Informações")

frame_info = ttk.Frame(root, padding="20")
frame_info.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_nome = ttk.Label(frame_info, text="Nome:")
label_nome.grid(column=0, row=0, sticky=tk.W)

entry_nome = ttk.Entry(frame_info, width=30)
entry_nome.grid(column=1, row=0)

label_nome_cachorro = ttk.Label(frame_info, text="Nome do Cachorro:")
label_nome_cachorro.grid(column=0, row=1, sticky=tk.W)

entry_nome_cachorro = ttk.Entry(frame_info, width=30)
entry_nome_cachorro.grid(column=1, row=1)

label_raca = ttk.Label(frame_info, text="Raça:")
label_raca.grid(column=0, row=2, sticky=tk.W)

entry_raca = ttk.Entry(frame_info, width=30)
entry_raca.grid(column=1, row=2)

label_idade = ttk.Label(frame_info, text="Idade:")
label_idade.grid(column=0, row=3, sticky=tk.W)

entry_idade = ttk.Entry(frame_info, width=30)
entry_idade.grid(column=1, row=3)

label_telefone = ttk.Label(frame_info, text="Telefone:")
label_telefone.grid(column=0, row=4, sticky=tk.W)

entry_telefone = ttk.Entry(frame_info, width=30)
entry_telefone.grid(column=1, row=4)

submit_button_info = ttk.Button(frame_info, text="Enviar", command=enviar_info)
submit_button_info.grid(column=0, row=5, columnspan=2)

root.mainloop()
