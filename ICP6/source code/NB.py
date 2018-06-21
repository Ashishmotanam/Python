from sklearn import naive_bayes, metrics
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split


irisdataset = datasets.load_iris()  #Loading iris dataset

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target
x_tr, x_tst, y_tr, y_tst = train_test_split(x, y, test_size=0.2) # creating train and test data

my_model= GaussianNB()
my_model.fit(x_tr,y_tr)  #fitting  train data for my model
y_pred = my_model.predict(x_tst)  #predicting test data
#print(y_pred)
print(metrics.accuracy_score(y_tst, y_pred))  # printing accuracy for predicted data and actual data

