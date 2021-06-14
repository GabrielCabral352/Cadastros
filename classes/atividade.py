import connection
import os


class Atividade:
    con = connection.conectar()

    def menu_atividade(self):
        os.system('cls')
        print('=====Atividade=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_atividade()
        elif int(opt) == 2:
            self.inserir_atividade(questao=input('Questão:'),
                                   id_modulo=input('ID Módulo:'),
                                   um=input('um:'),
                                   dois=input('dois:'),
                                   tres=input('tres:'),
                                   quatro=input('quatro:'),
                                   resposta=input('Resposta: '),
                                   numero=input('Numero: '),
                                   fk=input('Foreign Key Modulos: ')
                                   )
        elif int(opt) == 3:
            self.delete_cliente(id=input('ID:'))
        elif int(opt) == 4:
            self.update_cliente(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_atividade(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbatividade'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_atividade(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbatividade(questao,idmodulo,um,dois,tres,quatro,resposta,numero,fk_modulos_id) ' \
                  'values(%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['questao'], kwargs['id_modulo'], kwargs['um'], kwargs['dois'], kwargs['tres'],
                                 kwargs['quatro'], kwargs['resposta'], kwargs['numero'], kwargs['fk']))

            self.con.commit()
            cursor.close()

    def delete_atividade(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbatividade where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_cliente(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbatividade set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
