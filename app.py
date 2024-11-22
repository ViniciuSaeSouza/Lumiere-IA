import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Carregar modelos e scaler treinados a partir do caminho atualizado
classificacao_model = joblib.load('notebook/modelos/modelo_classificacao.pkl')
regressao_model = joblib.load('notebook/modelos/modelo_regressao.pkl')
scaler = joblib.load('notebook/modelos/scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/<model_type>', methods=['POST'])
def predict(model_type):
    # Pega os dados do JSON recebido
    data = request.get_json()
    consumo_anterior = float(data['Consumo_Anterior'])
    media_consumo = float(data['Media_consumo'])
    num_moradores = int(data['Num_moradores'])
    renda = float(data['Renda'])
    
    # Organiza os dados para o modelo
    nova_amostra = [[consumo_anterior, media_consumo, num_moradores, renda]]
    nova_amostra = scaler.transform(nova_amostra)  # Escalar os dados

    # Prever dependendo do tipo de modelo
    if model_type == 'classificacao':
        prediction = classificacao_model.predict(nova_amostra)
        # Se for 1, é Aumento, caso contrário, é Diminuição
        result = "Aumento" if prediction[0] == 1 else "Diminuição"
        return jsonify(prediction=f'Classificação: {result}')
    elif model_type == 'regressao':
        prediction = regressao_model.predict(nova_amostra)
        return jsonify(prediction=f'Consumo Futuro: {prediction[0]} kWh')

if __name__ == '__main__':
    app.run(debug=True)
