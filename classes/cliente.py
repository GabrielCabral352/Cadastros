import connection
import os


class Cliente:
    con = connection.conectar()

    def menu_cliente(self):
        os.system('cls')
        print('=====Cliente=====')
        print('1 - Listar')
        print('2 - Inserir')
        print('3 - Deletar')
        print('4 - Atualizar')
        opt = input()
        if int(opt) == 1:
            self.listagem_cliente()
        elif int(opt) == 2:
            self.inserir_cliente(nome=input('Nome:'),
                                 telefone=input('Telefone:'),
                                 email=input('Email:'),
                                 cpf=input('CPF:'),
                                 senha=input('Senha:'),
                                 autorizado=input('Autorizado:'),
                                 tipo=input('Tipo:'))
        elif int(opt) == 3:
            self.delete_cliente(id=input('ID:'))
        elif int(opt) == 4:
            self.update_cliente(coluna=input('Coluna:'), valor=input('Valor:'), id=input('ID:'))
        else:
            print('Valor Inválido')

    def listagem_cliente(self):
        with self.con.cursor() as cursor:
            sql = 'select * from tbcliente'
            cursor.execute(sql)
            dados = cursor.fetchall()
            self.con.commit()
            cursor.close()
            for linhas in dados:
                print(linhas)
        os.system('PAUSE')

    def inserir_cliente(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'insert into tbcliente(nome,telefone,email, cpf, senha, autorizado, tipo) ' \
                  'values(%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (kwargs['nome'], kwargs['telefone'], kwargs['email'], kwargs['cpf'],
                                 kwargs['senha'], kwargs['autorizado'], kwargs['tipo']))

            self.con.commit()
            cursor.close()

    def delete_cliente(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = 'delete from tbcliente where id = %s'
            print(kwargs)
            cursor.execute(sql, (kwargs['id']))
            self.con.commit()
            cursor.close()

    def update_cliente(self, **kwargs):

        with self.con.cursor() as cursor:
            sql = "update tbcliente set {} = %s where id = %s".format(kwargs['coluna'])
            cursor.execute(sql, (kwargs['valor'], kwargs['id']))
            self.con.commit()
            cursor.close()
