from train_test_api import Model


print('Start evaluation')
model_names = ['knn','random_forest','svc']
for name in model_names:
    print('----------------------------------')
    print('Model name: {0}'.format( name))
    model = Model(name)
    model.evaluate()
