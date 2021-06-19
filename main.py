import os

from classes.cliente import Cliente
from classes.administrador import Administrador
from classes.arquivo import Arquivo
from classes.atividade import Atividade
from classes.categoria import Categoria
from classes.curso import Curso
from classes.detalhemat import Detalhe
from classes.instrutor import Instrutor
from classes.matricula import Matricula
from classes.modulos import Modulo
from classes.notas import Nota

adm = Administrador()
cliente = Cliente()
arq = Arquivo()
atv = Atividade()
cat = Categoria()
cur = Curso()
det = Detalhe()
inst = Instrutor()
mat = Matricula()
mod = Modulo()
nota = Nota()


def menu():
    os.system('cls')
    print('=====MENU=====')
    print('1 - Cliente')
    print('2 - Administrador')
    print('3 - Arquivo')
    print('4 - Atividade')
    print('5 - Categoria')
    print('6 - Curso')
    print('7 - Instrutor')
    print('8 - Matricula')
    print('9 - Modulos')
    print('10 - Notas')
    print('0 - Sair')


while True:
    menu()
    op = input()
    if int(op) == 1:
        cliente.menu_cliente()
    elif int(op) == 2:
        adm.menu_adm()
    elif int(op) == 3:
        arq.menu_arq()
    elif int(op) == 4:
        atv.menu_atividade()
    elif int(op) == 5:
        cat.menu_cat()
    elif int(op) == 6:
        cur.menu_cur()
    elif int(op) == 7:
        inst.menu_inst()
    elif int(op) == 8:
        mat.menu_mat()
    elif int(op) == 9:
        mod.menu_mod()
    elif int(op) == 10:
        nota.menu_nota()
    elif int(op) == 0:
        exit()
    else:
        print('Valor Informádo é inválido')
        os.system('PAUSE')
