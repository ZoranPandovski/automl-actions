import mindsdb_native
import sys

print('HERE **************************')
print("PARAMETER: ", sys.argv[0])
# Train a predictor with quick_learn
predictor = mindsdb_native.Predictor(name='test_quick_interface')
predictor.quick_learn(
    from_data='https://raw.githubusercontent.com/mindsdb/mindsdb-examples/master/classics/home_rentals/dataset/test.csv',
    to_predict='rental_price',
    stop_training_in_x_seconds=20
)
