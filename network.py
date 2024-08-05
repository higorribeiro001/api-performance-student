import numpy as np
from keras.models import model_from_json

def rede_neural(novo):
    arquivo = open('regressor.json', 'r')
    
    estrutura_rede = arquivo.read()
    arquivo.close()
    
    regressor = model_from_json(estrutura_rede)
    regressor.load_weights('regressor.weights.h5')
    
    novo = np.array([novo])
    
    previsao = regressor.predict(novo)
    
    return previsao

#precisao: 83%
#loss: 0423
