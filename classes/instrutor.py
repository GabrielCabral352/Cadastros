import connection
import os


class Instrutor:
    con = connection.conectar()

    def menu_inst(self):
        os.system('cls')
        print('=====Instutor=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_inst()
        elif int(opt) == 2:
            self.inserir_inst(nome=input('Nome:'),
                              login=input('Login:'),
                              senha=input('Senha:'))
        elif int(opt) == 3:
            self.delete_inst(id=input('ID:'))
        elif int(opt) == 4:
            self.update_inst(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_inst(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbinstrutor'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_inst(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbinstrutor(nome,login,senha) values(%s,%s,%s)'
            cursor.execute(sql, (kwargs['nome'], kwargs['login'], kwargs['senha']))

            self.con.commit()
            cursor.close()

    def delete_inst(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbinstrutor where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_inst(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbinstrutor set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
