import numpy as np
from pyod.utils.data import generate_data

X_train, X_test, y_train, y_test = generate_data(
    n_train=400,
    n_test=100,
    n_features=2,
    contamination=0.1,
    random_state=42,
)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

x = X_train[:, 0]
y = X_train[:, 1]
