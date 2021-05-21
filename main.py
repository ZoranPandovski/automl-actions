import mindsdb_native
import sys
import os

# Read env variables send from GH Action
DATA = os.getenv('INPUT_DATASET')
TARGET = os.getenv('INPUT_TARGET')
STOP_TRAINING = os.getenv('INPUT_STOP_TRAINING')

# Train a new model
predictor = mindsdb_native.Predictor(name='model')
predictor.learn(
    to_predict=TARGET,
    from_data=DATA,
    stop_training_in_x_seconds=5
)
os.system("echo ::set-output name=prediction::itworks")
