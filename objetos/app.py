from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Brasileirinho', 'Marmita')

nova_bebida = Bebida('Suco de limão', 5.0, 'Médio')
prato = Prato('Aligot', 150.0, 'Pure de batatas com queijo')
restaurante_praca.adicionar_no_cardapio(nova_bebida)
restaurante_praca.adicionar_no_cardapio(prato)



def main():
    print(nova_bebida)
    



if __name__ == '__main__':
    main()