import pandas as pd
from sklearn.linear_model import LinearRegression

# sample data
data = pd.DataFrame({
    'hours': [1, 2, 3, 4, 5],
    'score': [40, 50, 60, 70, 80]
})

X = data[['hours']]
y = data['score']

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)

# prediction
print(model.predict([[6]]))
