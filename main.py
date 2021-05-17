import mindsdb_native
import sys
import os

DATA = os.getenv('INPUT_DATASET')
TARGET = os.getenv('INPUT_TARGET')

# Train a predictor with quick_learn
predictor = mindsdb_native.Predictor(name='test_quick_interface')
predictor.quick_learn(
    from_data=DATA,
    to_predict=TARGET,
    stop_training_in_x_seconds=5
)
