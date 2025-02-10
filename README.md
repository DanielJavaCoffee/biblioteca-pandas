# Case do Varejo

## Descrição do Dataset
O dataset é composto por informações de vendas de uma loja virtual que atua em todo o território nacional, vendendo produtos de diferentes departamentos. Além disso, a loja opera em diversos canais de venda, como marketplace, loja própria, entre outros.

## Premissas de Negócio
Ao analisar os dados, é importante considerar as seguintes premissas de negócio:

1. **Dados Faltantes de UF**: Devido a um erro no sistema, algumas compras não possuem informações de UF. Para solucionar o problema, foi decidido que essas compras serão consideradas como pertencentes ao estado de Mato Grosso do Sul (MS).
2. **Preço Final vs. Preço com Frete**: O preço final de um produto não pode ser maior do que o preço com frete.

## Métricas de Análise
Com base no contexto e nas premissas de negócio estabelecidas, podemos avaliar as seguintes métricas:

### 1. Departamentos Mais Vendidos
Analisando os dados de vendas, podemos identificar quais são os departamentos mais populares entre os clientes. Essa informação é útil para entender quais produtos são mais procurados e ajustar a estratégia de vendas da loja.

### 2. Média de Preço com Frete por Nome de Departamento
Para entender o comportamento de preço por departamento, calculamos a média de preço com frete por nome de departamento. Essa métrica ajuda a identificar os departamentos mais rentáveis e ajustar a precificação dos produtos de acordo com a margem de lucro desejada.

### 3. Quantidade de Vendas por Mês
Analisando a quantidade de vendas realizadas em cada mês, podemos identificar sazonalidades no comportamento dos clientes. Isso permite planejar campanhas de marketing específicas para cada período.

### 4. Média de Renda por Tipo de Canal de Venda
Identificar a média de renda dos clientes em diferentes canais de venda ajuda a loja a direcionar suas estratégias de marketing e vendas para cada público-alvo.

### 5. Média de Idade de Clientes por Bandeira
Saber a faixa etária dos clientes por bandeira ajuda a identificar perfis de consumidores e ajustar a abordagem de vendas para atender melhor cada público.

## Como Utilizar Este Projeto
1. **Instalação das Dependências**:
   Certifique-se de ter as bibliotecas necessárias instaladas. Execute o seguinte comando:
   ```bash
   pip install pandas matplotlib plotly
