# Criar Interface
import tkinter as tk
from ponto import *

Ponto = tk.Tk()
Ponto.title('Ponto')
Ponto.geometry('300x200')
Ponto.configure(background='#4682B4')

titulo = tk.Label(Ponto,text='Ponto',bg='#4682B4',fg='#000', font='verdana 25 bold').pack(side='top')
id = tk.Label(Ponto,font='verdana',text='Digite Seu ID',bg='#4682B4',fg='#000').place(y=55,x=95)

entry_id = tk.StringVar()
entrada = tk.Entry(Ponto,textvariable=entry_id,width=40).place(y=85,x=25)

def pegar_id():
  m = entry_id.get()
  print('ID_PEGO')
  return m

def btn_iniciar():
  id = pegar_id()
  hora_inicial(id)
  print('Seu Expediente Começou!')

def btn_finalizar():
  id = pegar_id()
  hora_final(id)
  finalizar_ponto(id)
  print('Seu Expediente Foi Finalizado!')

tk.Button(command=btn_iniciar,font='verdana',text="Iniciar",bg='#000000',fg='#DCDCDC',).place(y=120,x=70)
tk.Button(command=btn_finalizar,font='verdana',text="Finalizar",bg='#000000',fg='#DCDCDC',).place(y=120,x=160)

Ponto.mainloop()