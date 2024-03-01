# 1 -> classes e objetos
class Livro:

    def __init__(self, titulo, autor, ano):
        """__init__ é um método especial em Python. Ele é o construtor da classe. 
        Sempre que criamos uma instância de uma classe, este método é automaticamente chamado"""

        self.titulo = titulo
        """atribuindo o valor do parâmetro título a variável de instância titulo""" 
        self.autor = autor
        """atribuindo o valor do parâmetro autor a variável de instância autor"""
        self.ano = ano
        """atribuindo o valor do parâmetro ano a variável de instância ano""" 


meu_livro = Livro('1984', 'George Orwell', 1949)
"""instanciando (criando) um objeto da classe Livro e passando os valores"""

# 2 -> Atributos
# Acessando os atributos do objeto meu_livro:
print(meu_livro.titulo)
print(meu_livro.autor)
print(meu_livro.ano)

# 3 -> Métodos
class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo 
        self.autor = autor 
        self.ano = ano

    def descricao(self):
        """definindo um método chamado descricao: Este método retorna uma descrição formatada do livro."""

        return f'Título do livro: {self.titulo} \nAutor: {self.autor} \npublicado em: {self.ano}'
    """retornando uma string formatada que descreve o livro"""

meu_livro = Livro('1984', 'George Orwell', 1984)

print(meu_livro.descricao())
"""isso irá executar o método descricao definido na classe Livro e imprimir a descricao do livro"""