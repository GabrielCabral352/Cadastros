import connection
import os


class Matricula:
    con = connection.conectar()

    def menu_mat(self):
        os.system('cls')
        print('=====Matricula=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_mat()
        elif int(opt) == 2:
            self.inserir_mat(sit=input('Situação:'),
                             senha=input('Andamento:'),
                             nome=input('Data:'),
                             fk1=input('Foreign Key Curso'),
                             fk2=input('')
                             )
        elif int(opt) == 3:
            self.delete_mat(id=input('ID:'))
        elif int(opt) == 4:
            self.update_mat(coluna=input('Coluna:'),
                            valor=input('Valor:'),
                            id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_mat(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbmatricula'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_mat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbmatricula(sitacao,andamento,dat, fk_tbcurso_id, fk_tbcliente_id) values(%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['sit'], kwargs['senha'], kwargs['nome'], kwargs['fk1'], kwargs['fk2']))

            self.con.commit()
            cursor.close()

    def delete_mat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbmatricula where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_mat(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbmatricula set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
