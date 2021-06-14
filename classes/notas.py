import connection
import os


class Nota:
    con = connection.conectar()

    def menu_nota(self):
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
            self.inserir_mat(escolha=input('escolha:'),
                             resposta=input('resposta:'),
                             nota=input('nota:'),
                             fk_tbatividades_id=input('fk_tbatividades_id'),
                             fk_tbmodulos_id=input('fk_tbmodulos_id'),
                             fk_tbmatricula_id=input('fk_tbmatricula_id'),
                             fk_tbmatricula_idcurso=input('fk_tbmatricula_idcurso:')
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
            sql = 'insert into tbmatricula(user,senha,nome) values(%s,%s,%s)'
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
