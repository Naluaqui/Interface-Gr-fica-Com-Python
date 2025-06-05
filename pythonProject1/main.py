import customtkinter as ckt

ckt.set_appearance_mode('dark')

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'jhonathan' and senha == '123':
        resultado_login.configure(text='Login feito com sucesso!',
        text_color='green')

    else:
        resultado_login.configure(text='Login incorreto!',
        text_color='red')

app = ckt.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

label_usuario = ckt.CTkLabel(app,text='Usuario')
label_usuario.pack(pady=10)

campo_usuario = ckt.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

label_senha = ckt.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)

campo_senha = ckt.CTkEntry(app,placeholder_text='Digite sua senha')
campo_senha.pack(pady=10)

botao = ckt.CTkButton(app,text='login',command=validar_login)
botao.pack(pady=10)

resultado_login = ckt.CTkLabel(app,text='')
resultado_login.pack(pady=10)


app.mainloop()