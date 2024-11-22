# **Projeto Lumière, Previsão de Consumo de Energia**

Este repositório contém um aplicativo Flask para disponibilizar modelos de Machine Learning treinados para previsão de consumo de energia. O objetivo do projeto é demonstrar a integração entre os modelos de classificação e regressão, permitindo a realização de previsões em um ambiente web.

## **Tecnologias Utilizadas**
- **Flask**: Framework web para Python, utilizado para criar a API.
- **Scikit-learn**: Biblioteca utilizada para treinar os modelos de Machine Learning.
- **Joblib**: Biblioteca para carregar e salvar modelos treinados.
- **HTML & CSS**: Para a interface de usuário.

## **Arquitetura**
O sistema consiste em um servidor Flask que oferece dois tipos de modelos preditivos:
1. **Modelo de Classificação**: Previsão sobre o tipo de mudança no consumo de energia ("Aumento" ou "Diminuição").
2. **Modelo de Regressão**: Previsão do consumo de energia no futuro, dado o consumo histórico, média de consumo, número de moradores e a renda da família.

## **Instruções de Instalação**

1. **Clonando o repositório**
   ```bash
   git clone https://github.com/seu_usuario/projeto_consumo_energia.git
   cd projeto_consumo_energia
   ```

2. **Criando o Ambiente Virtual**
    Crie um ambiente virtual para o projeto. Caso ainda não tenha o `virtualenv` instalado, instale com:

    ```bash
    pip install virtualenv
    ```

    Crie o ambiente virtual:

    ```bash
    virtualenv venv
    ```

    Ative o ambiente virtual:

    - **No Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **No Linux ou MacOS:**

      ```bash
      source venv/bin/activate
      ```

3. **Instalando dependências**
   Você pode instalar as dependências necessárias usando o `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   Se o arquivo `requirements.txt` não existir, você pode instalar as dependências manualmente:
   ```bash
   pip install flask scikit-learn joblib
   ```

4. **Carregando os Modelos**
   Certifique-se de que os arquivos dos modelos treinados (`modelo_classificacao.pkl`, `modelo_regressao.pkl`, `scaler.pkl`) estejam na pasta `modelos/` conforme a estrutura do projeto.

## **Execução**

Para rodar o servidor Flask localmente, use o seguinte comando:

```bash
python app.py
```

O servidor será iniciado e estará disponível em `http://127.0.0.1:5000/`.

## **Interface Web**

A página inicial (`index.html`) contém dois botões, cada um para enviar dados para um dos modelos:

1. **Classificação**: Envia dados para o modelo de classificação, retornando "Aumento" ou "Diminuição" com base no consumo.
2. **Regressão**: Envia dados para o modelo de regressão, retornando o valor estimado para o consumo de energia no futuro.

### **Exemplo de entrada de dados**
- **Consumo_Anterior**: Consumo de energia no mês anterior (em kWh).
- **Média_consumo**: Média de consumo de energia nos meses anteriores (em kWh).
- **Num_moradores**: Número de moradores da residência.
- **Renda**: Renda da família (em R$).

### **Fluxo de Trabalho**
1. O usuário insere os dados nos campos de input.
2. Ao clicar no botão correspondente (Classificação ou Regressão), os dados são enviados para a API.
3. O modelo retorna a previsão e ela é exibida na mesma página.

## **Endpoints da API**

- **POST `/predict/classificacao`**: Previsão sobre a mudança no consumo de energia (Aumento ou Diminuição).
  - Entrada:
    ```json
    {
      "Consumo_Anterior": 150.0,
      "Media_consumo": 140.0,
      "Num_moradores": 4,
      "Renda": 3000.0
    }
    ```
  - Saída:
    ```json
    {
      "prediction": "Classificação: Aumento"
    }
    ```

- **POST `/predict/regressao`**: Previsão do consumo futuro (em kWh).
  - Entrada:
    ```json
    {
      "Consumo_Anterior": 150.0,
      "Media_consumo": 140.0,
      "Num_moradores": 4,
      "Renda": 3000.0
    }
    ```
  - Saída:
    ```json
    {
      "prediction": "Consumo Futuro: 155.0 kWh"
    }
    ```

## Autores

- Vinicius Souza - [GitHub](https://github.com/ViniciuSaeSouza)
- Laura de Oliveira Cintra - [GitHub](https://github.com/Laura-Cintra)
- Maria Eduarda Alves da Paixão - [GitHub](https://github.com/MariaEdPaixao)

## Contribuição

Sinta-se à vontade para fazer um fork do projeto e enviar PRs. Sugestões de melhorias são bem-vindas!

## **Conclusão**
Este projeto demonstra como integrar modelos de Machine Learning com uma aplicação web usando Flask, permitindo que o usuário envie dados e receba previsões diretamente pela interface.
