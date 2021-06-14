import connection
import os


class Modulo:
    con = connection.conectar()

    def menu_mod(self):
        os.system('cls')
        print('=====Modulo=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_mod()
        elif int(opt) == 2:
            self.inserir_mod(nome=input('nome:'),
                             sigla=input('sigla:'),
                             key=input('key:'),
                             fk1=input('Foreign Key Curso')
                             )
        elif int(opt) == 3:
            self.delete_mod(id=input('ID:'))
        elif int(opt) == 4:
            self.update_mod(coluna=input('Coluna:'),
                            valor=input('Valor:'),
                            id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_mod(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbmodulos'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_mod(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbmodulos(nome,sigla,palavrachave,fk_tbcurso_id) values(%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['nome'], kwargs['sigla'], kwargs['key'], kwargs['fk']))

            self.con.commit()
            cursor.close()

    def delete_mod(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbmodulos where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_mod(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbmodulos set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
