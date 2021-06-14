import connection
import os


class Curso:
    con = connection.conectar()

    def menu_cur(self):
        os.system('cls')
        print('=====Curso=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_cur()
        elif int(opt) == 2:
            self.inserir_cur(titulo=input('Titulo:'),
                             descricao=input('Descrição:'),
                             keyword=input('Palavra-Chave:'),
                             duracao=input('Duração:'),
                             pathPNG=input('Caminho PNG: '),
                             fk1=input('Foreign Key Categoria'),
                             fk2=input('Foreign Key Instrutor'))
        elif int(opt) == 3:
            self.delete_cur(id=input('ID:'))
        elif int(opt) == 4:
            self.update_cur(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_cur(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbcurso'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_cur(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbcurso(titulo,descricao,palavrachave,duracao,caminhoIMG,' \
                  'fk_tbcategoria_id,fk_tbinstrutor_id) values(%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['titulo'], kwargs['titulo'], kwargs['titulo'], kwargs['titulo'], kwargs['titulo'],
                                 kwargs['titulo'], kwargs['titulo']))

            self.con.commit()
            cursor.close()

    def delete_cur(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbcurso where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_cur(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbcurso set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
