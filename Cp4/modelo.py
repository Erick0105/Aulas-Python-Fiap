class Funcionario:
    def __init__(self, matricula: int = 0, nome: str = "", salario: float = 0):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
    
    def __str__(self):
        return f"""Matricula - ({self.matricula})\n - Nome: {self.nome}\n -  Salario: {self.salario}"""