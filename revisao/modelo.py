class Contato:
    def __init__(self, contato_id : int, nome : str = "", telefone : str = "", email : str = ""):
        self.contato_id = contato_id
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def __str__(self):
        return f"""({self.contato_id}) - {self.nome}\n{self.telefone}\n{self.email}"""
    
if __name__ == "__main__":
    c1 = Contato(1, "João Silva", "(11) 11111-1111", "joao@teste.com")
    print(c1)