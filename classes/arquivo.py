import connection
import os


class Arquivo:
    con = connection.conectar()

    def menu_arq(self):
        os.system('cls')
        print('=====Arquivo=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_arq()
        elif int(opt) == 2:
            self.inserir_arq(nome=input('Nome:'),
                             fk=input('Foreign Key Modulos:'))
        elif int(opt) == 3:
            self.delete_arq(id=input('ID:'))
        elif int(opt) == 4:
            self.update_arq(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_arq(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbarquivo'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)

        os.system('PAUSE')

    def inserir_arq(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbarquivo(nome,fk_tbmodulos_id) values(%s,%s)'
            cursor.execute(sql, (kwargs['nome'], kwargs['fk']))

            self.con.commit()
            cursor.close()

    def delete_arq(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbarquivo where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_arq(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbarquivo set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
