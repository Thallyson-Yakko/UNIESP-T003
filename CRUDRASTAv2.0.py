import customtkinter
from tkinter import *
from  tkinter import Toplevel, messagebox, END

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

class AlunoCRUD:
    def __init__(self, root):
        self.root = root
        self.root.geometry('900x600')
        self.root.title('CRUD de notas do RASTA')
        self.root.iconbitmap('icon.ico')
        self.root.resizable(False, False)

        # Logo Uniesp

        img = PhotoImage(file='background.png')
        label_img = customtkinter.CTkLabel(master=self.root, image=img, text=None)
        label_img.place(x=0, y=0)

        # Frame

        self.frame = customtkinter.CTkFrame(master=self.root, width=395, height=600)
        self.frame.pack(side=RIGHT)

        # Frame widgets

        self.label = customtkinter.CTkLabel(master=self.frame, text='Cadastro de Alunos', font=('Roboto', 20, 'bold'), text_color=('white'))
        self.label.place(x=115, y=25)

        # Campos de entrada

        self.usuario = customtkinter.CTkEntry(master=self.frame, placeholder_text='Nome do usuario', width=300, font=('Roboto', 14))
        self.usuario.place(x=25, y=105)
        self.validacao1 = customtkinter.CTkLabel(master=self.frame, text='*O campo nome do usuario é obrigatorio.', text_color='green', font=('Roboto', 12))
        self.validacao1.place(x=25, y=135)

        self.matricula = customtkinter.CTkEntry(master=self.frame, placeholder_text='Matricula', width=300, font=('Roboto', 14))
        self.matricula.place(x=25, y=165)
        self.validacao2 = customtkinter.CTkLabel(master=self.frame, text='*O campo matricula é obrigatorio.', text_color='green', font=('Roboto', 12))
        self.validacao2.place(x=25, y=195)

        self.nota = customtkinter.CTkEntry(master=self.frame, placeholder_text='Nota 1', width=300, font=('Roboto', 14))
        self.nota.place(x=25, y=225)
        self.validacao3 = customtkinter.CTkLabel(master=self.frame, text='*O campo Nota 1 é obrigatorio.', text_color='green', font=('Roboto', 12))
        self.validacao3.place(x=25, y=255)

        self.nota2 = customtkinter.CTkEntry(master=self.frame, placeholder_text='Nota 2', width=300, font=('Roboto', 14))
        self.nota2.place(x=25, y=285)
        self.validacao4 = customtkinter.CTkLabel(master=self.frame, text='*O campo Nota 2 é obrigatorio.', text_color='green', font=('Roboto', 12))
        self.validacao4.place(x=25, y=315)

        self.nota3 = customtkinter.CTkEntry(master=self.frame, placeholder_text='Nota 3', width=300, font=('Roboto', 14))
        self.nota3.place(x=25, y=345)
        self.validacao5 = customtkinter.CTkLabel(master=self.frame, text='*O campo Nota 3 é obrigatorio.', text_color='green', font=('Roboto', 12))
        self.validacao5.place(x=25, y=375)

        self.sexo = customtkinter.CTkEntry(master=self.frame, placeholder_text='Sexo', width=145, font=('Roboto', 14))
        self.sexo.place(x=25, y=405)

        self.idade = customtkinter.CTkEntry(master=self.frame, placeholder_text='Idade', width=145, font=('Roboto', 14))
        self.idade.place(x=185, y=405)
        self.validacao6 = customtkinter.CTkLabel(master=self.frame, text='*O campo Sexo e Idade são obrigatorios.', text_color='green', font=('Roboto', 12))
        self.validacao6.place(x=25, y=440)

        self.button_cadastrar = customtkinter.CTkButton(master=self.frame, text='Cadastrar', width=300, corner_radius=32, fg_color='#9e0921', hover_color='#580412', command=self.cadastrar_aluno)
        self.button_cadastrar.place(x=25, y=475)

        self.button_atualizar = customtkinter.CTkButton(master=self.frame, text='Atualizar', width=300, corner_radius=32, fg_color='#9e0921', hover_color='#580412', command=self.atualizar_aluno)
        self.button_atualizar.place(x=25, y=515)

        self.button_apagar = customtkinter.CTkButton(master=self.frame, text='Apagar', width=300, corner_radius=32, fg_color='#9e0921', hover_color='#580412', command=self.apagar_aluno)
        self.button_apagar.place(x=25, y=555)


#Função Cadastro do Aluno
        

    def cadastrar_aluno(self):
        nome = self.usuario.get()
        matricula = self.matricula.get()
        nota = float(self.nota.get())
        nota2 = float(self.nota2.get())
        nota3 = float(self.nota3.get())
        sexo = self.sexo.get()
        idade = self.idade.get()
        media = (nota + nota2 + nota3) / 3
        messagebox.showinfo("Média do Aluno", f"A média do aluno é: {media:.2f}")

        if nome and matricula and nota and nota2 and nota3 and sexo and idade:
            
            #Salvando em um arquivo TXT

            with open("alunos.txt", "a") as file:
                file.write(f"{nome}, {matricula}, {nota}, {nota2}, {nota3}, {media:.2f}, {sexo}, {idade}\n")

    
            # Limpar campos
                
            self.limpar_campos()


# Crie uma nova janela (pop-up) para edição


    def abrir_janela_edicao(self):
        janela_edicao = customtkinter.CTkToplevel(self.root)
        janela_edicao.title("Editar Aluno")
        janela_edicao.resizable(False, False)
        janela_edicao.geometry('350x320')

        # Campos de edição na nova janela

        usuario_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Nome do usuário', width=300, font=('Roboto', 14))
        usuario_edit.place(x=25, y=25)
        matricula_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Matrícula', width=300, font=('Roboto', 14))
        matricula_edit.place(x=25, y=65)
        nota_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Nota 1', width=300, font=('Roboto', 14))
        nota_edit.place(x=25, y=105)
        nota2_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Nota 2', width=300, font=('Roboto', 14))
        nota2_edit.place(x=25, y=145)
        nota3_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Nota 3', width=300, font=('Roboto', 14))
        nota3_edit.place(x=25, y=185)
        sexo_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Sexo', width=145, font=('Roboto', 14))
        sexo_edit.place(x=25, y=225)
        idade_edit = customtkinter.CTkEntry(master=janela_edicao, placeholder_text='Idade', width=145, font=('Roboto', 14))
        idade_edit.place(x=185, y=225)

        # Preencher os campos de edição com os dados do aluno selecionado

        matricula_a_editar = self.matricula.get()  # Usar Matricula
        with open("alunos.txt", "r") as file:
            for linha in file:
                dados_aluno = linha.strip().split(", ")
                if dados_aluno[1] == matricula_a_editar:
                    usuario_edit.insert(0, dados_aluno[0])
                    matricula_edit.insert(0, dados_aluno[1])
                    nota_edit.insert(0, dados_aluno[2])
                    nota2_edit.insert(0, dados_aluno[3])
                    nota3_edit.insert(0, dados_aluno[4])
                    sexo_edit.insert(0, dados_aluno[5])
                    idade_edit.insert(0, dados_aluno[6])
                    break

        
        button_confirmar_edicao = customtkinter.CTkButton(master=janela_edicao, text='Confirmar Edição', width=300, corner_radius=32, fg_color='#9e0921', hover_color='#580412', command=lambda: self.confirmar_edicao(janela_edicao, usuario_edit.get(), matricula_edit.get(), nota_edit.get(), nota2_edit.get(), nota3_edit.get(), sexo_edit.get(), idade_edit.get()))                                                                                                                                                                                                                                                                                                                                                            
        button_confirmar_edicao.place(x=25, y=265)
        
        

    def atualizar_aluno(self):
        self.abrir_janela_edicao()


#Apagar Aluno


    def apagar_aluno(self):
        matricula_a_apagar = self.matricula.get()  # Use o identificador correto

        # Ler os dados do arquivo
        with open("alunos.txt", "r") as file:
            linhas = file.readlines()

        # Escrever de volta no arquivo, excluindo a linha correspondente à matrícula
        with open("alunos.txt", "w") as file:
            for linha in linhas:
                dados_aluno = linha.strip().split(", ")
                if dados_aluno[1] != matricula_a_apagar:
                    file.write(linha)

        # Limpar os campos
        self.limpar_campos()


#Limpar os Campos  


    def limpar_campos(self):
        self.usuario.delete(0, END)
        self.matricula.delete(0, END)
        self.nota.delete(0, END)
        self.nota2.delete(0, END)
        self.nota3.delete(0, END)
        self.sexo.delete(0, END)
        self.idade.delete(0, END)

if __name__ == "__main__":
    janela = customtkinter.CTk()
    AlunoCRUD(janela)
    janela.mainloop()