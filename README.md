# Restaurant Orders

Este é um projeto para a construção de uma ferramenta de gestão de cardápios para o restaurante Spaghetti Shrimp Chapa Quente Curry Shallow Pan of Food. O objetivo é fornecer uma maneira simples de gerar cardápios levando em consideração restrições alimentares e disponibilidade de ingredientes em estoque. Atualmente, a gestão das receitas e do estoque do restaurante é realizada de forma ineficiente através de arquivos CSV, e este projeto visa melhorar essa gestão.

## Funcionalidades

O projeto está sendo desenvolvido em Python e consiste em diferentes classes com funcionalidades específicas:

### 1. Testando classes já implementadas - Parte 1

Nesta etapa, serão criados testes para a classe `Ingredient` no arquivo `tests/ingredient/test_ingredient.py`. Os testes devem garantir o seguinte:

- A classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- O atributo `restrictions` é populado como esperado;
- O método mágico `__repr__` funciona como esperado;
- O método mágico `__eq__` funciona como esperado;
- O método mágico `__hash__` funciona como esperado.

### 2. Testando classes já implementadas - Parte 2

Nesta etapa, serão criados testes para a classe `Dish` no arquivo `tests/dish/test_dish.py`. Os testes devem garantir o seguinte:

- A classe pode ser instanciada corretamente de acordo com a assinatura esperada;
- Os métodos da classe, incluindo os métodos mágicos, funcionam como esperado;
- O dicionário de receita do prato retorna a quantidade correta de um ingrediente;
- São levantados erros ao criar pratos inválidos.

### 3. Mapeamento Pratos <> Ingredientes

Nesta etapa, será implementada uma nova classe que será responsável pelo mapeamento dos pratos e suas respectivas receitas (ingredientes e quantidades). A classe receberá o caminho para um arquivo CSV no parâmetro `source_path`. Serão feitas as seguintes implementações:

- A classe fará a leitura do arquivo CSV e instanciará os pratos e ingredientes correspondentes;
- A classe conterá o atributo `dishes`, que será um conjunto (`set`) com todos os pratos devidamente instanciados;
- Cada prato conterá sua respectiva receita, ou seja, os ingredientes e quantidades, bem como seu preço.

### 4. Geração dos cardápios

Nesta etapa, será implementada uma classe responsável pela geração dos cardápios. Serão feitas as seguintes implementações:

- A classe poderá ser instanciada corretamente;
- O método `get_main_menu` retornará uma lista de dicionários com o cardápio completo quando nenhum parâmetro for passado;
- O método `get_main_menu` retornará uma lista de dicionários com o cardápio correto, respeitando a restrição alimentar passada como parâmetro.

## Configuração do ambiente

Para garantir a qualidade do código, recomenda-se o uso do linter Flake8. Para executá-lo localmente no projeto, execute o seguinte comando:

```
python3 -m flake8
```



O Python oferece um recurso chamado ambiente virtual que permite a execução de diferentes tipos de projetos com diferentes versões de bibliotecas, sem conflitos. Para configurar o ambiente virtual, siga os passos abaixo:

1. Crie o ambiente virtual:
   ```
   python3 -m venv .venv
   ```

2. Ative o ambiente virtual:
   ```
   source .venv/bin/activate
   ```

3. Instale as dependências no ambiente virtual:
   ```
   python3 -m pip install -r dev-requirements.txt
   ```

Certifique-se de ativar o ambiente virtual sempre que estiver trabalhando no projeto. Para desativar o ambiente virtual, execute o comando `deactivate`.

## Executando os testes

Certifique-se de ter ativado o ambiente virtual antes de executar os testes.

Para executar todos os testes:
```
python3 -m pytest
```

Para executar um arquivo de teste específico, utilize o seguinte comando:
```
python3 -m pytest tests/nomedoarquivo.py
```

## Considerações finais

Este projeto tem como objetivo melhorar a gestão de cardápios do restaurante Spaghetti Shrimp Chapa Quente Curry Shallow Pan of Food. Ao final da implementação, espera-se que a ferramenta seja capaz de gerar cardápios de forma simples e considerando restrições alimentares e disponibilidade de ingredientes em estoque. O código deve seguir boas práticas de desenvolvimento, ser legível e de fácil manutenção.
