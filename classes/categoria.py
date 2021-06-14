import connection
import os


class Categoria:
    con = connection.conectar()

    def menu_cat(self):
        os.system('cls')
        print('=====Categoria=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_cat()
        elif int(opt) == 2:
            self.inserir_cat(cat=input('Categoria do Curso'))
        elif int(opt) == 3:
            self.delete_cat(id=input('ID:'))
        elif int(opt) == 4:
            self.update_cat(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_cat(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbcategoria'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_cat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbcategoria(categoriacurso) values(%s)'
            cursor.execute(sql, (kwargs['cat']))

            self.con.commit()
            cursor.close()

    def delete_cat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbcategoria where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_cat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbcategoria set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
