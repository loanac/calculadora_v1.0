from tkinter import * 
from tkinter import ttk 


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.resizable(False,False)


# frames 
frame_tela= Frame(janela, width=235, height=50, bg= "#001829")
frame_tela.grid(row=0, column=0)

frame_display= Frame(janela, width=235, height=268, bg="#001829")
frame_display.grid(row=1, column=0)



# label
valor_texto= StringVar()
calc_label= Label(frame_tela, textvariable=valor_texto,width=16,height=2,padx=7,relief=FLAT,anchor="e",justify=RIGHT,font=('Ivy 18'),bg="#001829",fg="white")
calc_label.place(x=0,y=0)


t_valores = ''

#funcao
def entraValor(event):
    global t_valores
    
    t_valores= t_valores + str(event)
    
    #mostrar no frame
    valor_texto.set(t_valores)
    
def calcular():
    global t_valores
    resultado = eval(t_valores)
    
    valor_texto.set(str(resultado))
    
#funcao limpar tela
def limpaTela():
    global t_valores
    t_valores= ""
    valor_texto.set("")

# botões 1 linha
bt1 = Button(frame_display, text="C", command=limpaTela,font='Ivy 13 bold', width=12, height=2, relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)

bt2 = Button(frame_display, text="%", command=lambda:entraValor('%'), font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt2.place(x=118, y=0)

bt3 = Button(frame_display, text="/",command=lambda:entraValor('/'),font='Ivy 13 bold',width=5, height=2, relief=RAISED, overrelief=RIDGE, bg="#1e5267", fg="white")
bt3.place(x=177, y=0)

# botoes 2 linha (4)
bt4 = Button(frame_display, text="7",command=lambda:entraValor('7'),font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt4.place(x=0, y=52)

bt5 = Button(frame_display, text="8",command=lambda:entraValor('8'),font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt5.place(x=59, y=52)

bt6 = Button(frame_display, text="9", command=lambda:entraValor('9'),font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt6.place(x=118, y=52)

bt7 = Button(frame_display, text="*", command=lambda:entraValor('*'),font='Ivy 13 bold',width=5, height=2, relief=RAISED, overrelief=RIDGE, bg="#1e5267", fg="white")
bt7.place(x=177, y=52)


# linha 3 bt
bt8 = Button(frame_display, text="4", command=lambda:entraValor('4'),font='Ivy 13 bold', width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt8.place(x=0, y=104)

bt9 = Button(frame_display, text="5", command=lambda:entraValor('5'),font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt9.place(x=59, y=104)

bt10 = Button(frame_display, text="6",command=lambda:entraValor('6'),font='Ivy 13 bold', width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt10.place(x=118, y=104)

bt11 = Button(frame_display, text="-",command=lambda:entraValor('-'),font='Ivy 13 bold', width=5, height=2, relief=RAISED, overrelief=RIDGE, bg="#1e5267", fg="white")
bt11.place(x=177, y=104)


# linha 4 
bt12 = Button(frame_display, text="1",command=lambda:entraValor('1'),font='Ivy 13 bold', width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt12.place(x=0, y=156)

bt13 = Button(frame_display, text="2",command=lambda:entraValor('2'), font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt13.place(x=59, y=156)

bt14 = Button(frame_display, text="3", command=lambda:entraValor('3'),font='Ivy 13 bold',width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt14.place(x=118, y=156)

bt15 = Button(frame_display, text="+", command=lambda:entraValor('+'),font='Ivy 13 bold', width=5, height=2, relief=RAISED, overrelief=RIDGE, bg="#1e5267", fg="white")
bt15.place(x=177, y=156)

# última
bt16 = Button(frame_display, text="0", command=lambda:entraValor('0'),font='Ivy 13 bold', width=12, height=2, relief=RAISED, overrelief=RIDGE)
bt16.place(x=0, y=208)

bt17 = Button(frame_display, text=".",command=lambda:entraValor('.'),font='Ivy 13 bold', width=5,height=2,relief=RAISED, overrelief=RIDGE)
bt17.place(x=118, y=208)

bt18 = Button(frame_display, text="=", command=calcular,font='Ivy 13 bold', width=5, height=2, relief=RAISED, overrelief=RIDGE, bg="#1e5267", fg="white")
bt18.place(x=177, y=208)

 
janela.mainloop()