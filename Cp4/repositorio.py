import os
import oracledb
from oracledb import Connetion
from modelo import Funcionario

class Repositorio():
    def __init__(self):
        self.usuario = os.environ.get("FIAP_ORACLE_USER")
        self.senha = os.environ.get("FIAP_ORACLE_PASS")   
        self.url = "oracle.fiap.com.br:1521/orcl"
    
    def gerar_conexao(self):
        conex = oracledb.connect(user=self.usuario,password=self.senha, dsn= self.url)
        return conex
    
    def gravar(self, func: Funcionario):

        conexao = gerar_conexao()
        cursor = conectar.cursor()
        
        try:
            comand_sql = """INSERT INTO funcionario (matricula, nome, salario) values (:1, :2, :3)"""
            cursor.execute(comand_sql, (func.matricula, func.nome, func.salario))
            conexao.commmit()
            
        except err:
            print(err)
            cursor.rollback()

        return True

    def pesquisar(self, nome: str) -> list:
        
        conexao = gerar_conexao()
        cursor = conectar.cursor()
        lista = []
        
        try:
            comand_sql = """SELECT * FROM funcionario WHERE nome LIKE :1"""
            cursor.execute(comand_sql, ("%" + nome + "%"))
            
        except err:
            print(err)
            cursor.rollback()
            
            
        for dados in cursor:
            matricula = dados[0]
            nome = dados[1]
            salario = dados[2]

            func = Funcionario(matricula, nome, salario)

            lista.append(func)
        
        conexao.commmit()
        return lista