from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Brasileirinho', 'Marmita')

nova_bebida = Bebida('Suco de limão', 5.0, 'Médio')
prato = Prato('Aligot', 150.0, 'Pure de batatas com queijo')
nova_bebida.aplicar_desconto()
prato.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(nova_bebida)
restaurante_praca.adicionar_no_cardapio(prato)



def main():
    restaurante_praca.exibir_cardapio
    



if __name__ == '__main__':
    main()