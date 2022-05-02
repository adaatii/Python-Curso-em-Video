# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seje capaz de funcionar como a função imput(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from d112.utilidadescev import moeda
from d112.utilidadescev import dado


p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 10)

