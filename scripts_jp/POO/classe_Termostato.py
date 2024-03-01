"""
Exemplo prático com uma classe que representa um termostato simples em uma sala. 

Descrição: 

Imagine um termostato que controla a temperatura em uma sala. Esse termostato permite que você aumente, diminua, configure
ou leia a temperatura atual. 

Vamos cirar uma classe para este termostato e definir alguns métodos para interagir com ele.
"""

class Termostato:

    def __init__(self, temperatura_atual=20):
        
        self.temperatura_atual = temperatura_atual

    def aumentar_temperatura(self, valor):
        """método que aumenta a temperatura do termostato"""

        self.temperatura_atual += valor # Adiciona o valor fornecido ao atributo 'temperatura_atual'

        print(f'Temperatura aumentada em {valor}°. Nova temperatura: {self.temperatura_atual}.')

    def diminuir_temperatura(self, valor):
        """método que diminui a temperatura do termostato"""

        self.temperatura_atual -= valor # Subtrai o valor fornecido do atributo 'temperatura_atual'

        print(f'Temperatura diminuida em {valor}°. Nova temperatura: {self.temperatura_atual}')

    def configurar_temperatura(self, nova_temperatura):
        """método para configurar (definir) a temperatura"""

        self.temperatura_atual = nova_temperatura # Define a 'temperatura_atual' para o novo valor fornecido

        print(f'Temperatura configurada para {nova_temperatura}°.')

    def mostrar_temperatura(self):
        """método para exibir a temperatura atual"""

        print(f'Temperatura atual: {self.temperatura_atual}')
        
meu_termostato = Termostato() # Instanciando um termostato 

meu_termostato.aumentar_temperatura(5) 

meu_termostato.diminuir_temperatura(5)

meu_termostato.configurar_temperatura(10)

meu_termostato.mostrar_temperatura()
