##### Desenvolvendo Funções Principais

from datetime import datetime
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123',
    database='bateponto'
)

def hora_atual():
  hora_atual = datetime.now()
  return hora_atual

def hora_inicial(nome):
  curso = conexao.cursor()
  comando = f"update funcionarios set hora_inicial = '{hora_atual()}' where nome = '{nome}';"
  curso.execute(comando)
  print("Hora Inicial Marcada com Sucesso")

def hora_final(nome):
  curso = conexao.cursor()
  comando = f"update funcionarios set hr_final = '{hora_atual()}' where nome = '{nome}';"
  curso.execute(comando)
  print("Hora Final Marcada com Sucesso")

def calculo_diferenca_hora():
  pass

def finalizar_ponto():
  pass

hora_final("Miguel")
