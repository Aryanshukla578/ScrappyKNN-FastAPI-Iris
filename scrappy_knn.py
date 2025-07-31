# scrappy_knn.py
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
