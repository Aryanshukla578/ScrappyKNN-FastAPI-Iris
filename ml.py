from numpy import may_share_memory
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from scipy.spatial import distance
from scipy.spatial import distance
class ScrappyKNN():
    def fit(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train
    def predict(self, features_test):
        predictions = []
        for row in features_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    def closest(self, row):
        best_dist = self.euc(row, self.features_train[0])
        best_index = 0
        for i in range(1, len(self.features_train)):
            dist = self.euc(row, self.features_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.labels_train[best_index]
    def euc(self, row1, row2):
        return distance.euclidean(row1, row2)

iris_dataset=datasets.load_iris()
#print(iris_dataset)
features = iris_dataset.data
labels = iris_dataset.target
#print(features)
#print(labels)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.5)
my_classifier = ScrappyKNN()
#my_classifier = KNeighborsClassifier()
my_classifier.fit(features_train, labels_train)
prediction = my_classifier.predict(features_test)
print("Acuuracy is:",accuracy_score(labels_test, prediction))
#versicolor
iris1=[[4.7,4.4,4.5,4.2]]
iris_prediction=my_classifier.predict(iris1)
print(iris_prediction)
if iris_prediction[0]==0:
    print("setosa")
elif iris_prediction[0]==1:
    print("versicolor")
elif iris_prediction[0]==2:
    print("virginica")
