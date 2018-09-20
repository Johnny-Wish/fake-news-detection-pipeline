from sklearn.neural_network import MLPClassifier
# if mlp_config cannot be loaded, make sure to append "PROJECT_ROOT/model" in your `PYTHONPATH` variable
from mlp_config import sizes
from mlp_config import random_seed as seed

model = MLPClassifier()
param_dist = {
    "hidden_layer_sizes": sizes,
    "activation": ["logistic", "tanh", "relu"],
    "solver": ["adam"],
    "alpha": [0, 1e-4, 1e-3, 1e-2],
    "learning_rate_init": [1e-4, 1e-3, 1e-2],
    "random_state": [seed],
    "max_iter": [100, 200, 500],
    "beta_1": [0.5, 0.8, 0.9, 0.999],
    "beta_2": [0.9, 0.999, 0.99999],
}
