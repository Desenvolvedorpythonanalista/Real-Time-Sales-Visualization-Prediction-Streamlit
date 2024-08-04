from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def treinar_modelo(X_train, y_train):
    """Treina o modelo de regressão linear e retorna o modelo."""
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo

def avaliar_modelo(modelo, X_test, y_test):
    """Avalia o modelo com base no conjunto de testes e retorna o erro quadrático médio (MSE)."""
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse
