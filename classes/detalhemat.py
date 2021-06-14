import connection
import os


class Detalhe:
    con = connection.conectar()

    def menu_detalhe(self):
        os.system('cls')
        print('=====Cliente=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_detalhe()
        elif int(opt) == 2:
            self.inserir_detalhe(nome=input('Nome:'),
                                 video=input('Video:'),
                                 tempo=input('Tempo:'),
                                 modulo=input('Modulo:'),
                                 fk1=input('Foreign Key Modulo'),
                                 fk2=input('Foreign Key Matricula')
                                 )
        elif int(opt) == 3:
            self.delete_detalhe(id=input('ID:'))
        elif int(opt) == 4:
            self.update_detalhe(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_detalhe(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbdetalhemat'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_detalhe(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbdetalhemat(nome,video,tempo,modulo,fk_tbmodulos_id,fk_tbmatricula_id) ' \
                  'values(%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['nome'], kwargs['video'], kwargs['tempo'], kwargs['modulo'], kwargs['fk1'],
                                 kwargs['fk2']))

            self.con.commit()
            cursor.close()

    def delete_detalhe(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbdetalhemat where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_detalhe(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbdetalhemat set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
