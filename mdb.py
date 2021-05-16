import mindsdb_native
import sys

print('HERE **************************')
print("PARAMETER1: ", sys.argv[0])
print("PARAMETER2: ", sys.argv[1])
# Train a predictor with quick_learn
predictor = mindsdb_native.Predictor(name='test_quick_interface')
predictor.quick_learn(
    from_data=sys.argv[0],
    to_predict=sys.argv[1],
    stop_training_in_x_seconds=5
)
