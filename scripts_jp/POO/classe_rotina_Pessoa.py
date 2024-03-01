"""
-> Exercicio simulando a rotina de uma pessoa. 

Implemente métodos para as seguintes ações: 

-> acordar(): Faz a pessoa acordar, se já não estiver acordada

-> comer(): Permite que a pessoa coma, desde que não esteja dirigindo ou dormindo

-> parar_de_comer(): Faz a pessoa parar de comer, se estiver comendo.

-> dirigir(): Permite que a pessoa dirija, desde que não esteja comendo ou dormindo

-> parar_de_dirigir(): Faz a pessoa parar de dirigir, se estiver dirigindo

-> dormir(): Permite que a pessoa durma, desde que não esteja comendo ou dirigindo
"""

class Pessoa:

    def __init__(self, nome):
        
        self.nome = nome 
        self.acordado = False
        self.comendo = False
        self.dirigindo = False

    def acordar(self):
        """método para fazer a pessoa acordar"""

        if self.acordado: # verifica se a pessoa já está acordada

            print(f'{self.nome} já está acordado.') # Se sim, exibe que a pessoa já está acordada

        else:

            self.acordado = True # Se não, muda o estado "acordado" para True

            print(f'{self.nome} acordou.') # exibe que a pessoa acordou

    def comer(self):
        """método para fazer a pessoa comer"""

        if self.dirigindo: # verifica se a pessoa está dirigindo

            print(f'{self.nome} não pode comer enquanto dirige.')

        elif not self.acordado: # verifica se a pessoa está dormindo

            print(f'{self.nome} não pode comer enquanto está dormindo.')
        
        elif self.comendo: # verifica se a pessoa está comendo

            print(f'{self.nome} já está comendo.')

        else:

            self.comendo = True # se todas as condições acima não forem verdadeiras, então muda o status "comendo" para True

            print(f'{self.nome} começou a comer.') # exibe uma mensagem informando que a pessoa começou a comer

    def parar_de_comer(self):
        """método para fazer a pessoa parar de comer"""

        if not self.comendo: # verifica se a pessoa não está comendo

            print(f'{self.nome} não está comendo no momento.') # se sim, imprime que a pessoa não está comendo

        else:

            self.comendo = False # se a pessoa estiver comendo, então ela pode parar de comer

            print(f'{self.nome} terminou de comer.') # exibe que a pessoa parou de comer

    def dirigir(self):
        """método para fazer a pessoa dirigir"""

        if not self.acordado: # verifica se a pessoa está dormindo

            print(f'{self.nome} não pode dirigir enquanto está dormindo.')

        elif self.comendo: # verifica se a pessoa está comendo

            print(f'{self.nome} não deve dirigir enquanto está comendo.')

        elif self.dirigindo: # verifica se a pessoa já está dirigindo

            print(f'{self.nome} já está dirigindo.') 

        else:

            self.dirigindo = True # se as condições acima não forem verdadeiras, então muda o status dirigindo para True

            print(f'{self.nome} começou a dirigir.') # exibe uma mensagem informando que a pessoa começou a dirigir

    def parar_de_dirigir(self):
        """método para fazer a pessoa parar de dirigir"""

        if not self.dirigindo: # verifica se a pessoa está dirigindo

            print(f'{self.nome} não está dirigindo.')

        else:

            self.dirigindo = False # se a pessoa estiver dirigindo, muda o status para False e ela pode parar de dirigir

            print(f'{self.nome} parou de dirigir.')

    def dormir(self):
        """método para fazer a pessoa dormir"""

        if self.dirigindo: # verifica se a pessoa está dirigindo 

            print(f'{self.nome} não pode dormir enquanto dirige.')

        elif self.comendo: # verifica se a pessoa está comendo

            print(f'{self.nome} não pode dormir enquanto come.')

        elif not self.acordado: # verifica se a pessoa já está dormindo

            print(f'{self.nome} já está dormindo.')

        else: # se nenhuma das condições acima forem verdadeiras, a pessoa pode dormir.

            print(f'{self.nome} foi dormir.')

            self.acordado = False # alteramos o status "acordado"para False 

            self.comendo = False  # alteramos o status "comendo" para False



joao = Pessoa('João')

joao.acordar()

joao.comer()

joao.parar_de_comer()

joao.dirigir()

joao.parar_de_dirigir()

joao.dormir()
