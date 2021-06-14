import connection
import os


class Administrador:
    con = connection.conectar()

    def menu_adm(self):
        os.system('cls')
        print('=====Adiministrador=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_adm()
        elif int(opt) == 2:
            self.inserir_adm(user=input('User:'),
                             senha=input('Senha:'),
                             nome=input('Nome:'))
        elif int(opt) == 3:
            self.delete_adm(id=input('ID:'))
        elif int(opt) == 4:
            self.update_adm(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_adm(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbadministrador'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_adm(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbadministrador(user,senha,nome) values(%s,%s,%s)'
            cursor.execute(sql, (kwargs['user'], kwargs['senha'], kwargs['nome']))

            self.con.commit()
            cursor.close()

    def delete_adm(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbadministrador where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_adm(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbadministrador set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
