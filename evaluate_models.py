from train_test_api import Model
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt



def plot_conf_matrix(conf_matrix, accuracy):       
    print(model.model_name)
    df_cm = pd.DataFrame(conf_matrix, index = [i for i in "ABCDEF"],
                  columns = [i for i in "ABCDEF"])
    plt.figure(figsize = (10,7))
    plt.title('Model: '+model.model_name + ' Accuracy: '+ str(accuracy))
    sn.set(font_scale=1.4)#for label size
    sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size    
    plt.show()



print('Start evaluation')
model_names = ['knn','random_forest','svc']
for name in model_names:
    print('----------------------------------')
    print('Model name: {0}'.format( name))
    model = Model(name)
    train_time, test_time, accuracy_train, accuracy_test, conf_matrix = model.evaluate()
    plot_conf_matrix(conf_matrix, accuracy_test)
    print('Accuracy test: {0}'.format(accuracy_test))
    print('Accuracy train: {0}'.format(accuracy_train))
    print("test time:  {0}s".format(test_time))
    print("train time: {0}s".format(train_time))



